import requests

from modules.ai_indexer import AIIndexer
from modules.prompt_builder import PromptBuilder


class ChatEngine:

    def __init__(self):

        self.indexer = AIIndexer()

        self.prompt_builder = PromptBuilder()

        self.url = "http://localhost:11434/api/generate"

    def ask(self, report_id, question):

        chunks = self.indexer.search(
            report_id,
            question
        )

        context = ""

        for chunk in chunks:

            context += chunk["text"]

            context += "\n\n"

            prompt = self.prompt_builder.build_prompt(
                context,
                question
            )

            payload = {

                "model": "llama3.2:3b",

                "prompt": prompt,

                "stream": False

            }

            response = requests.post(

                self.url,

                json=payload

            )

            return response.json()["response"]