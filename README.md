# DriveWise: Metadata-Aware Automotive RAG Assistant

A conversational AI system that helps users understand car brochures by answering natural language queries using brochure-grounded information.

## What it does

- User selects a car brand and model
- Asks questions in plain English (mileage, safety, price, features etc)
- System retrieves relevant brochure sections using metadata filtering
- Re-ranks results and generates an answer grounded in the brochure data
- Shows source attribution (which section and page the answer came from)

## Features

- **Metadata filtering** - searches only within the selected car's brochure
- **Structured chunking** - brochure split by sections (engine, safety, mileage etc)
- **Re-ranking** - re-scores retrieved chunks for better relevance
- **Context window control** - limits context to avoid noise
- **Source attribution** - shows where the answer came from
- **Evaluation metrics** - faithfulness and context relevance scores
- **Query logging** - tracks all queries and response times
- **Web UI** - Streamlit-based interactive interface

## Tech Stack

- **Embeddings**: sentence-transformers (all-MiniLM-L6-v2)
- **Vector Store**: ChromaDB (with metadata filtering)
- **Web UI**: Streamlit
- **Language**: Python

## How to Run

### Web App (Streamlit)
```
cd DriveWise
streamlit run app.py
```

### Notebook
Open `DriveWise_Final_Project.ipynb` in Jupyter Notebook and run all cells.

## Project Structure

```
DriveWise/
├── app.py                          # Streamlit web app
├── rag_engine.py                   # Core RAG pipeline
├── brochure_data.py                # Sample brochure data
├── DriveWise_Final_Project.ipynb   # Notebook for submission
├── requirements.txt                # Dependencies
└── README.md                       # This file
```

## Cars Included

| Brand | Models |
|-------|--------|
| Hyundai | Creta, Venue, i20 |
| Tata | Nexon, Harrier |
| Maruti Suzuki | Brezza |

## Architecture

```
User Query → Metadata Filter → Vector Search → Re-Rank → Context Control → Answer + Sources
```
