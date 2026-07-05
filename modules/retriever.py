from modules.embedding_engine import (
    EmbeddingEngine
)

from modules.vector_store import (
    VectorStore
)


class Retriever:

    def __init__(self):

        self.embedding_engine = EmbeddingEngine()

        self.vector_store = VectorStore()

    def build_report_index(

        self,

        report_id,

        chunks

    ):

        embeddings = self.embedding_engine.generate_embeddings(
            chunks
        )

        self.vector_store.create_index(
            embeddings
        )

        self.vector_store.metadata = chunks

        self.vector_store.save_index(
            report_id
        )

    def retrieve(

        self,

        report_id,

        question

    ):

        self.vector_store.load_index(
            report_id
        )

        query_embedding = self.embedding_engine.generate_embedding(
            question
        )

        return self.vector_store.search(query_embedding )