from modules.chat_engine import ChatEngine

chat = ChatEngine()

answer = chat.ask(

    report_id=1,

    question="What is the hemoglobin level?"

)

print()

print(answer)
