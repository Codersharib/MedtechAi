from sentence_transformers import SentenceTransformer
import numpy as np


class EmbeddingEngine:

    def __init__(self):

        print("Loading Embedding Model...")

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        print("Embedding Model Loaded")

    def generate_embedding(self, text):

        embedding = self.model.encode(text)

        return np.array(
            embedding,
            dtype="float32"
        )

    def generate_embeddings(self, chunks):

        texts = []

        for chunk in chunks:

            texts.append(
                chunk["text"]
            )

        embeddings = self.model.encode(texts)

        return np.array(
            embeddings,
            dtype="float32"
        )
