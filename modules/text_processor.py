import re


class TextProcessor:

    def __init__(self, chunk_size=500, overlap=100):

        self.chunk_size = chunk_size
        self.overlap = overlap

    def clean_text(self, text):

        if not text:
            return ""

        # Normalize line endings
        text = text.replace("\r", "\n")

        # Remove multiple blank lines
        text = re.sub(
            r"\n+",
            "\n",
            text
        )

        # Remove multiple spaces
        text = re.sub(
            r"[ \t]+",
            " ",
            text
        )

        return text.strip()

    def create_chunks(self, text):

        text = self.clean_text(text)

        chunks = []

        start = 0

        chunk_id = 1

        while start < len(text):

            end = start + self.chunk_size

            chunk_text = text[start:end]

            metadata = {

                "chunk_id": chunk_id,

                "text": chunk_text,

                "start_char": start,

                "end_char": min(
                    end,
                    len(text)
                ),

                "length": len(chunk_text)

            }

            chunks.append(metadata)

            chunk_id += 1

            start += (
                self.chunk_size
                - self.overlap
            )

        return chunks
