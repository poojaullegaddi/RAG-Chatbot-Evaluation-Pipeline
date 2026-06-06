import pandas as pd

from rag.chatbot import get_rag_answer

df = pd.read_csv(
    "data/test_data.csv"
)

answers = []
contexts = []

for question in df["question"]:

    answer, context = get_rag_answer(
        question
    )

    answers.append(answer)

    contexts.append([context])

df["answer"] = answers

df["contexts"] = contexts

df.to_csv(
    "results.csv",
    index=False
)

print("Answers Generated")