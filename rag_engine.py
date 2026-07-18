# DriveWise RAG Engine
# handles all the retrieval and answer generation logic

import chromadb
import numpy as np
import time
import json
import logging
from datetime import datetime
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from brochure_data import brochures

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("drivewise_logs.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("DriveWise")


class DriveWiseRAG:
    def __init__(self):
        logger.info("Initializing DriveWise RAG engine...")
        start = time.time()

        # load embedding model
        self.embed_model = SentenceTransformer('all-MiniLM-L6-v2')
        logger.info("Embedding model loaded")

        # setup chromadb with persistent storage
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(
            name="car_brochures",
            metadata={"hnsw:space": "cosine"}
        )

        # ingest brochure data
        self._ingest_brochures()

        elapsed = time.time() - start
        logger.info(f"DriveWise initialized in {elapsed:.2f}s")

        # query log for tracking
        self.query_log = []

    def _ingest_brochures(self):
        """load all brochure chunks into chromadb with metadata"""
        documents = []
        metadatas = []
        ids = []
        idx = 0

        for brand, models in brochures.items():
            for model, sections in models.items():
                for section_name, section_data in sections.items():
                    text = section_data["text"]
                    page = section_data["page"]

                    documents.append(text)
                    metadatas.append({
                        "brand": brand,
                        "model": model,
                        "section": section_name,
                        "page": page,
                        "doc_id": f"{brand}_{model}_{section_name}"
                    })
                    ids.append(f"chunk_{idx}")
                    idx += 1

        # embed and add to collection
        embeddings = self.embed_model.encode(documents).tolist()
        self.collection.add(
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )

        logger.info(f"Ingested {idx} brochure chunks into vector store")
        self.total_chunks = idx

    def get_available_brands(self):
        """return list of brands we have data for"""
        return list(brochures.keys())

    def get_models_for_brand(self, brand):
        """return models available for a given brand"""
        if brand in brochures:
            return list(brochures[brand].keys())
        return []

    def retrieve(self, query, brand=None, model=None, top_k=5):
        """retrieve relevant chunks with optional metadata filtering"""
        start = time.time()

        # build metadata filter
        where_filter = None
        if brand and model:
            where_filter = {"$and": [
                {"brand": {"$eq": brand}},
                {"model": {"$eq": model}}
            ]}
        elif brand:
            where_filter = {"brand": {"$eq": brand}}

        # query chromadb
        query_embedding = self.embed_model.encode([query]).tolist()
        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=top_k,
            where=where_filter,
            include=["documents", "metadatas", "distances"]
        )

        elapsed = time.time() - start

        # format results
        retrieved = []
        if results["documents"] and results["documents"][0]:
            for i in range(len(results["documents"][0])):
                retrieved.append({
                    "text": results["documents"][0][i],
                    "metadata": results["metadatas"][0][i],
                    "distance": results["distances"][0][i],
                    "relevance_score": 1 - results["distances"][0][i]  # cosine distance to similarity
                })

        logger.info(f"Retrieved {len(retrieved)} chunks in {elapsed:.3f}s for query: '{query[:50]}...'")
        return retrieved

    def rerank(self, query, retrieved_chunks, top_k=3):
        """re-rank retrieved chunks using cross-similarity scoring"""
        if not retrieved_chunks:
            return []

        query_emb = self.embed_model.encode([query])
        chunk_texts = [c["text"] for c in retrieved_chunks]
        chunk_embs = self.embed_model.encode(chunk_texts)

        # compute cosine similarity between query and each chunk
        similarities = cosine_similarity(query_emb, chunk_embs)[0]

        # add rerank score to each chunk and sort
        for i, chunk in enumerate(retrieved_chunks):
            chunk["rerank_score"] = float(similarities[i])

        reranked = sorted(retrieved_chunks, key=lambda x: x["rerank_score"], reverse=True)
        logger.info(f"Re-ranked {len(reranked)} chunks, top score: {reranked[0]['rerank_score']:.4f}")
        return reranked[:top_k]

    def control_context_window(self, chunks, max_chars=2000):
        """keep only the most relevant chunks that fit within the context window"""
        selected = []
        total_chars = 0

        for chunk in chunks:
            if total_chars + len(chunk["text"]) <= max_chars:
                selected.append(chunk)
                total_chars += len(chunk["text"])
            else:
                break

        logger.info(f"Context window: {len(selected)} chunks, {total_chars} chars")
        return selected

    def generate_answer(self, query, context_chunks):
        """generate answer from the retrieved context
        using extractive approach -- pulls the most relevant sentences"""
        if not context_chunks:
            return "I couldn't find relevant information for your question in the brochure."

        # combine context
        context = " ".join([c["text"] for c in context_chunks])

        # split into sentences
        sentences = []
        for s in context.replace(". ", ".\n").split("\n"):
            s = s.strip()
            if len(s) > 15:
                sentences.append(s)

        if not sentences:
            return context[:500]

        # score each sentence against the query
        query_emb = self.embed_model.encode([query])
        sent_embs = self.embed_model.encode(sentences)
        scores = cosine_similarity(query_emb, sent_embs)[0]

        # pick top 3-4 most relevant sentences
        scored = list(zip(sentences, scores))
        scored.sort(key=lambda x: x[1], reverse=True)
        top_sentences = [s for s, _ in scored[:4]]

        # reorder them to match original document flow
        ordered = [s for s in sentences if s in top_sentences]
        answer = " ".join(ordered)

        return answer

    def ask(self, query, brand=None, model=None):
        """full RAG pipeline: retrieve -> rerank -> context control -> generate"""
        start = time.time()
        logger.info(f"Processing query: '{query}' | Brand: {brand} | Model: {model}")

        try:
            # step 1: retrieve with metadata filtering
            retrieved = self.retrieve(query, brand=brand, model=model, top_k=5)

            if not retrieved:
                result = {
                    "answer": "No brochure data found for the selected car. Please check the brand and model.",
                    "sources": [],
                    "response_time": time.time() - start,
                    "status": "no_data"
                }
                self._log_query(query, brand, model, result)
                return result

            # step 2: re-rank
            reranked = self.rerank(query, retrieved, top_k=3)

            # step 3: control context window
            final_chunks = self.control_context_window(reranked, max_chars=2000)

            # step 4: generate answer
            answer = self.generate_answer(query, final_chunks)

            # step 5: prepare source attribution
            sources = []
            for chunk in final_chunks:
                sources.append({
                    "brand": chunk["metadata"]["brand"],
                    "model": chunk["metadata"]["model"],
                    "section": chunk["metadata"]["section"],
                    "page": chunk["metadata"]["page"],
                    "relevance": round(chunk["rerank_score"], 4)
                })

            elapsed = time.time() - start
            result = {
                "answer": answer,
                "sources": sources,
                "response_time": round(elapsed, 3),
                "chunks_retrieved": len(retrieved),
                "chunks_used": len(final_chunks),
                "status": "success"
            }

            self._log_query(query, brand, model, result)
            return result

        except Exception as e:
            elapsed = time.time() - start
            logger.error(f"Error processing query: {e}")
            result = {
                "answer": f"Error: {str(e)}",
                "sources": [],
                "response_time": round(elapsed, 3),
                "status": "error"
            }
            self._log_query(query, brand, model, result)
            return result

    def _log_query(self, query, brand, model, result):
        """log every query for monitoring"""
        log_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "query": query,
            "brand": brand,
            "model": model,
            "status": result["status"],
            "response_time": result["response_time"],
            "chunks_used": result.get("chunks_used", 0)
        }
        self.query_log.append(log_entry)
        logger.info(f"Query logged: status={result['status']}, time={result['response_time']}s")

    def get_query_stats(self):
        """return stats from the query log"""
        if not self.query_log:
            return {"total_queries": 0}

        total = len(self.query_log)
        success = sum(1 for q in self.query_log if q["status"] == "success")
        failed = sum(1 for q in self.query_log if q["status"] in ["error", "no_data"])
        avg_time = np.mean([q["response_time"] for q in self.query_log])

        return {
            "total_queries": total,
            "successful": success,
            "failed": failed,
            "avg_response_time": round(avg_time, 3),
            "queries": self.query_log
        }

    def evaluate_response(self, query, answer, context_chunks):
        """basic evaluation of answer quality"""
        if not context_chunks or not answer:
            return {"faithfulness": 0, "context_relevance": 0}

        # faithfulness: how much of the answer is grounded in context
        context_text = " ".join([c["text"] for c in context_chunks]).lower()
        answer_words = answer.lower().split()
        grounded_words = sum(1 for w in answer_words if w in context_text and len(w) > 3)
        faithfulness = grounded_words / max(len(answer_words), 1)

        # context relevance: average rerank score
        avg_relevance = np.mean([c.get("rerank_score", 0) for c in context_chunks])

        return {
            "faithfulness": round(faithfulness, 3),
            "context_relevance": round(float(avg_relevance), 3)
        }
