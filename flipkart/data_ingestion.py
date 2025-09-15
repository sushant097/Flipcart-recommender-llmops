from langchain_astradb import AstraDBVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from flipkart.data_converter import DataConverter
from flipkart.config import Config


class DataIngestor:
    def __init__(self):
        self.embedding = HuggingFaceEmbeddings(model_name=Config.EMBEDDING_MODEL_NAME)

        self.vector_store = AstraDBVectorStore(
            embedding=self.embedding,
            collection_name="flipkart_databse",
            api_endpoint=Config.ASTRA_DB_API_ENDPOINT,
            token=Config.ASTRA_DB_APPLICATION_TOKEN,
            namespace=Config.ASTRA_DB_KEYSPACE,
        )

    def ingest(self, load_existing: bool = True):
        if load_existing:
            self.vector_store

        data_converter = DataConverter(file_path=Config.DATA_FILE_PATH)
        documents = data_converter.convert()

        self.vector_store.add_documents(documents)
        return self.vector_store
