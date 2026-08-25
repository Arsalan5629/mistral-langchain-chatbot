from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI(
    model_name="mistral-small-2506",
    api_key="Your API Key Here"
)

response = model.invoke("Explain Machine learnign")

print(response.content)