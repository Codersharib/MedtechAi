import os
import pickle
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer
from modules.text_processor import TextProcessor


class AIIndexer:

    def __init__(self):

        print("Loading Embedding Model...")

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.processor = TextProcessor()

        os.makedirs(
            "vector_store/indexes",
            exist_ok=True
        )

        os.makedirs(
            "vector_store/metadata",
            exist_ok=True
        )

        print("AI Indexer Ready")

    def create_index(
    self,
    report_id,
    text
):

        chunks = self.processor.create_chunks(
            text
        )

        chunk_texts = []

        for chunk in chunks:
            chunk_texts.append(
                chunk["text"]
            )

            embeddings = self.model.encode(
                chunk_texts,
                convert_to_numpy=True
            )

            embeddings = np.array(
                embeddings,
                dtype="float32"
            )

            dimension = embeddings.shape[1]

            index = faiss.IndexFlatL2(
                dimension
            )

            index.add(
                embeddings
            )

            faiss.write_index(
                index,
                f"vector_store/indexes/report_{report_id}.index"
            )

            with open(
                f"vector_store/metadata/report_{report_id}.pkl",
                "wb"
            ) as file:

                pickle.dump(
                    chunks,
                    file
                )

                print(
                    f"Index Created for Report {report_id}"
                )

        return True

    def load_index(
        self,
        report_id
    ):

        index = faiss.read_index(
            f"vector_store/indexes/report_{report_id}.index"
        )

        with open(
            f"vector_store/metadata/report_{report_id}.pkl",
            "rb"
        ) as file:

            metadata = pickle.load(
                file
            )

        return index, metadata

    def search(
        self,
        report_id,
        question,
        top_k=3
    ):

        index, metadata = self.load_index(
            report_id
        )

        query_embedding = self.model.encode(
            [question],
            convert_to_numpy=True
        )

        query_embedding = np.array(
            query_embedding,
            dtype="float32"
        )

        distances, indices = index.search(
            query_embedding,
            top_k
        )

        results = []

        for idx in indices[0]:

            if idx < len(metadata):

                results.append(
                    metadata[idx]
                )

        return results