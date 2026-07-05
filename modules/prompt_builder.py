class PromptBuilder:

    def build_prompt(
        self,
        context,
        question
    ):

        prompt = f"""

        You are MedIntel AI.

        You are an intelligent medical report assistant.

        Answer ONLY using the medical report context.

        If the answer is not available,

        say:

            "I could not find that information inside the uploaded report."

            -------------------------

            Medical Report Context

            {context}

            -------------------------

            Question

            {question}

            Answer:

                """

        return prompt