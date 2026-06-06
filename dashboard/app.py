import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="RAG Evaluation Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 RAG Chatbot Evaluation Dashboard")

# Load evaluation results
df = pd.read_csv("evaluation_results.csv")

# Display raw results
st.subheader("📋 Evaluation Results")
st.dataframe(df, use_container_width=True)

st.divider()

# Metrics Section
st.subheader("📈 Overall Metrics")

metrics = [
    "answer_relevancy",
    "faithfulness",
    "context_precision",
    "answer_correctness"
]

available_metrics = [
    metric for metric in metrics
    if metric in df.columns
]

cols = st.columns(len(available_metrics) + 1)

# Display average scores
for i, metric in enumerate(available_metrics):

    avg_score = round(
        df[metric].mean(),
        2
    )

    cols[i].metric(
        metric.replace("_", " ").title(),
        avg_score
    )

# Hallucination Rate
if "faithfulness" in df.columns:

    hallucinations = len(
        df[df["faithfulness"] < 0.7]
    )

    hallucination_rate = round(
        (hallucinations / len(df)) * 100,
        2
    )

    cols[-1].metric(
        "Hallucination Rate %",
        hallucination_rate
    )

st.divider()

# Low scoring examples
st.subheader("⚠️ Low Scoring Responses")

if "answer_correctness" in df.columns:

    low_scores = df[
        df["answer_correctness"] < 0.5
    ]

    if len(low_scores) == 0:

        st.success(
            "No low-scoring responses found."
        )

    else:

        for index, row in low_scores.iterrows():

            with st.expander(
                f"Question {index + 1}"
            ):

                st.write("### Question")
                st.write(row["question"])

                st.write("### Generated Answer")
                st.write(row["answer"])

                if "ground_truth" in row:
                    st.write("### Ground Truth")
                    st.write(row["ground_truth"])

                st.write("### Answer Correctness")
                st.write(
                    round(
                        row["answer_correctness"],
                        2
                    )
                )

                if "faithfulness" in row:
                    st.write("### Faithfulness")
                    st.write(
                        round(
                            row["faithfulness"],
                            2
                        )
                    )

st.divider()

st.caption(
    "Built with LangChain, FAISS, Groq, RAGAS and Streamlit"
)