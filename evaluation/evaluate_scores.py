import pandas as pd

import ast

from datasets import Dataset

from ragas import evaluate

from ragas.metrics import (
    answer_relevancy,
    faithfulness,
    context_precision,
    answer_correctness
)

from evaluation.ragas_config import (
    evaluator_llm,
    embeddings
)

df = pd.read_csv(
    "results.csv"
)

df["contexts"] = df["contexts"].apply(
    ast.literal_eval
)

dataset = Dataset.from_dict(
    {
        "question": df["question"].tolist(),
        "answer": df["answer"].tolist(),
        "contexts": df["contexts"].tolist(),
        "ground_truth": df["ground_truth"].tolist()
    }
)

result = evaluate(
    dataset,
    metrics=[
        answer_relevancy,
        faithfulness,
        context_precision,
        answer_correctness
    ],
    llm=evaluator_llm,
    embeddings=embeddings
)

print(result)

result_df = result.to_pandas()

result_df.to_csv(
    "evaluation_results.csv",
    index=False
)