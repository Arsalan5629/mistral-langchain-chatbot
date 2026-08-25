from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI(
    model_name="mistral-small-2506",
    api_key="S4vlDbyPQoK1NI9osGYUzmTwOf7MPe0C"
)

response = model.invoke("Explain Machine learnign")

print(response.content)