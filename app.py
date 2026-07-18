# DriveWise - Streamlit Web App
# run with: streamlit run app.py

import streamlit as st
import json
import time
from rag_engine import DriveWiseRAG

st.set_page_config(
    page_title="DriveWise - Car Brochure Assistant",
    page_icon="🚗",
    layout="wide"
)

# custom css
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1a1a2e;
        text-align: center;
        padding: 1rem 0;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .source-box {
        background-color: #f0f2f6;
        padding: 10px 15px;
        border-radius: 8px;
        margin: 5px 0;
        border-left: 4px solid #4CAF50;
    }
    .answer-box {
        background-color: #000000;
        padding: 20px;
        border-radius: 10px;
        margin: 15px 0;
        font-size: 1.05rem;
        line-height: 1.6;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# initialize the RAG engine (cached so it only loads once)
@st.cache_resource
def load_engine():
    return DriveWiseRAG()

engine = load_engine()

# header
st.markdown('<div class="main-header">🚗 DriveWise</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Metadata-Aware Automotive RAG Assistant — Ask anything about car brochures</div>', unsafe_allow_html=True)

# sidebar for car selection
with st.sidebar:
    st.header("🔧 Select Your Car")

    brands = engine.get_available_brands()
    selected_brand = st.selectbox("Brand", ["All Brands"] + brands)

    if selected_brand != "All Brands":
        models = engine.get_models_for_brand(selected_brand)
        selected_model = st.selectbox("Model", ["All Models"] + models)
    else:
        selected_model = "All Models"

    st.divider()
    st.header("📊 Session Stats")
    stats = engine.get_query_stats()
    col1, col2 = st.columns(2)
    col1.metric("Queries", stats["total_queries"])
    col2.metric("Avg Time", f"{stats.get('avg_response_time', 0)}s")

    if stats["total_queries"] > 0:
        st.metric("Success Rate", f"{(stats['successful']/stats['total_queries'])*100:.0f}%")

    st.divider()
    st.caption("DriveWise uses RAG to answer questions from car brochure data. No external APIs used.")

# main area
st.markdown("### Ask a question about your car")

# sample questions
sample_questions = [
    "What is the mileage of this car?",
    "What safety features does it have?",
    "What are the engine specifications?",
    "How much boot space does it have?",
    "What is the price range?",
    "Does it have a sunroof?",
    "What infotainment features are available?",
]

col1, col2 = st.columns([3, 1])
with col1:
    query = st.text_input("Your question:", placeholder="e.g. What is the mileage of Hyundai Creta?")
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    ask_button = st.button("Ask DriveWise 🚀", use_container_width=True)

# quick question buttons
st.markdown("**Quick questions:**")
cols = st.columns(4)
for i, sq in enumerate(sample_questions[:4]):
    if cols[i].button(sq, key=f"sample_{i}"):
        query = sq

if query and (ask_button or query):
    # figure out brand/model filters
    brand_filter = selected_brand if selected_brand != "All Brands" else None
    model_filter = selected_model if selected_model != "All Models" else None

    with st.spinner("Searching brochures..."):
        result = engine.ask(query, brand=brand_filter, model=model_filter)

    # show the answer
    st.markdown("### 💬 Answer")
    st.markdown(f'<div class="answer-box">{result["answer"]}</div>', unsafe_allow_html=True)

    # show metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Response Time", f'{result["response_time"]}s')
    col2.metric("Chunks Retrieved", result.get("chunks_retrieved", 0))
    col3.metric("Chunks Used", result.get("chunks_used", 0))

    # show sources
    if result["sources"]:
        st.markdown("### 📄 Sources")
        for i, src in enumerate(result["sources"]):
            section_name = src["section"].replace("_", " ").title()
            st.markdown(
                f'<div class="source-box">'
                f'<strong>{src["brand"]} {src["model"]}</strong> — {section_name} '
                f'(Page {src["page"]}) — Relevance: {src["relevance"]:.2%}'
                f'</div>',
                unsafe_allow_html=True
            )

    # evaluation
    with st.expander("📈 Response Evaluation"):
        # re-retrieve for evaluation
        retrieved = engine.retrieve(query, brand_filter, model_filter, top_k=3)
        reranked = engine.rerank(query, retrieved, top_k=3)
        eval_result = engine.evaluate_response(query, result["answer"], reranked)

        ecol1, ecol2 = st.columns(2)
        ecol1.metric("Faithfulness", f'{eval_result["faithfulness"]:.1%}')
        ecol2.metric("Context Relevance", f'{eval_result["context_relevance"]:.1%}')

# query log section
with st.expander("📋 Query Log"):
    stats = engine.get_query_stats()
    if stats["total_queries"] > 0:
        for log in reversed(stats["queries"]):
            st.text(
                f"[{log['timestamp']}] {log['query'][:60]}... "
                f"| {log['brand']}/{log['model']} "
                f"| {log['status']} | {log['response_time']}s"
            )
    else:
        st.info("No queries yet. Ask a question to get started!")
