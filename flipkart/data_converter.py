import pandas as pd
from langchain_core.documents import Document

class DataConverter:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def convert(self):
        df = pd.read_csv(self.file_path)[["product_title", "review"]]

        documents = []
        for _, row in df.iterrows():
            content = Document(page_content=row["review"], metadata={"prodct_name": row["product_title"]})
            documents.append(content)

        return documents