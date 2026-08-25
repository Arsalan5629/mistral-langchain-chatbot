from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage , SystemMessage
load_dotenv()

model = ChatMistralAI(
    model_name="mistral-small-2506",
    api_key="Your API Key Here"
)

messages = [
    SystemMessage(content="You are a helpful assistant.")
]

print("----------Welcome to the Chatbot! Type '0' to exit.-----------")

while True:
    
    prompt = input("You : ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot :",response.content)

print(messages)