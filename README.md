# 📊 RAG Chatbot Evaluation Pipeline

An end-to-end AI evaluation framework for measuring the performance of Retrieval-Augmented Generation (RAG) systems using **Groq**, **LangChain**, **FAISS**, **HuggingFace Embeddings**, **RAGAS**, and **Streamlit**.

This project automatically generates answers from a RAG chatbot, evaluates them using multiple RAGAS metrics, detects hallucinations, and visualizes results through an interactive dashboard.

---

## 🚀 Features

✅ PDF-based Knowledge Base

✅ Retrieval-Augmented Generation (RAG)

✅ FAISS Vector Database

✅ Groq LLM Integration

✅ Automated Answer Generation

✅ RAGAS-based Evaluation

✅ Hallucination Detection

✅ Interactive Streamlit Dashboard

✅ Identification of Low-Scoring Responses

---

## 🏗️ Architecture

```text
Knowledge Base PDF
        │
        ▼
Document Loading
        │
        ▼
Text Chunking
        │
        ▼
Embeddings Generation
        │
        ▼
FAISS Vector Store
        │
        ▼
Retriever
        │
        ▼
Groq LLM
        │
        ▼
Generated Answers
        │
        ▼
RAGAS Evaluation
        │
        ▼
Streamlit Dashboard
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Core Development |
| LangChain | RAG Pipeline |
| Groq | LLM Inference |
| FAISS | Vector Database |
| HuggingFace Embeddings | Text Embeddings |
| RAGAS | Evaluation Framework |
| Streamlit | Dashboard |
| Pandas | Data Processing |

---

## 📂 Project Structure

```text
RAG_Chatbot_Evaluation/
│
├── data/
│   ├── knowledge_base.pdf
│   └── test_data.csv
│
├── vector_store/
│   ├── __init__.py
│   ├── ingest.py
│   └── faiss_index/
│
├── rag/
│   ├── __init__.py
│   ├── chatbot.py
│   └── retriever.py
│
├── evaluation/
│   ├── __init__.py
│   ├── evaluator.py
│   ├── evaluate_scores.py
│   └── ragas_config.py
│
├── dashboard/
│   └── app.py
│
├── results.csv
├── evaluation_results.csv
├── requirements.txt
├── .env
└── README.md
```

---

## 📚 Build Vector Database

Load PDF documents, generate embeddings, and create a FAISS vector store.

```bash
python vector_store/ingest.py
```

Expected Output:

```text
Vector DB Created
```

---

## 🤖 Generate Answers

Run the RAG chatbot against the evaluation dataset.

```bash
python -m evaluation.evaluator
```

Expected Output:

```text
Answers Generated
```

Creates:

```text
results.csv
```

---

## 📈 Evaluate Responses

Run RAGAS evaluation metrics.

```bash
python -m evaluation.evaluate_scores
```

Example Output:

```text
{
    'answer_relevancy': 0.91,
    'faithfulness': 0.95,
    'context_precision': 0.89,
    'answer_correctness': 0.92
}
```

Creates:

```text
evaluation_results.csv
```

---

## 📊 Launch Dashboard

```bash
streamlit run dashboard/app.py
```

Dashboard Features:

- Evaluation Results Table
- Average Metrics
- Hallucination Rate
- Low Scoring Responses
- Interactive Visualization

---

## 📏 Evaluation Metrics

### Answer Correctness

Measures similarity between generated answer and ground truth.

### Answer Relevancy

Measures how well the answer addresses the user's question.

### Faithfulness

Measures whether the answer is grounded in retrieved context.

### Context Precision

Measures the relevance of retrieved documents.

### Hallucination Rate

Percentage of responses with low faithfulness scores.

---

## 🎯 Sample Use Case

Given a PDF knowledge base:

```text
What is RAG?
```

The system:

1. Retrieves relevant chunks.
2. Sends context to Groq LLM.
3. Generates answer.
4. Evaluates answer quality.
5. Displays performance metrics.

---

## 📸 Screenshots

### Dashboard

Add screenshot here:

```text
assets/dashboard.png
```

### Evaluation Results

Add screenshot here:

```text
assets/results.png
```

---
