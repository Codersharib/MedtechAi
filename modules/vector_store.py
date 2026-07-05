import os
import faiss
import pickle


class VectorStore:

    def __init__(self):

        self.index = None

        self.metadata = []

    def create_index(self, embeddings):

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.index.add(
            embeddings
        )


    def save_index(
        self,
        report_id
    ):

        os.makedirs(
            "vector_store/indexes",
            exist_ok=True
        )

        os.makedirs(
            "vector_store/metadata",
            exist_ok=True
        )

        faiss.write_index(

            self.index,

            f"vector_store/indexes/report_{report_id}.index"

        )

        with open(

            f"vector_store/metadata/report_{report_id}.pkl",

            "wb"

        ) as file:

            pickle.dump(
                self.metadata,
                file
            )


    def load_index(
        self,
        report_id
    ):

        self.index = faiss.read_index(

            f"vector_store/indexes/report_{report_id}.index"

        )

        with open(

            f"vector_store/metadata/report_{report_id}.pkl",

            "rb"

        ) as file:

            self.metadata = pickle.load(
                file
            )


    def search(
        self,
        query_embedding,
        top_k=3
    ):

        distances, indices = self.index.search(

            query_embedding.reshape(1, -1),

            top_k

        )

        results = []

        for index in indices[0]:

            results.append(

                self.metadata[index]

            )

        return results
