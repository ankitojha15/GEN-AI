from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini", temperature=1)

result = model.invoke("What is the capital of India")

print(result.content)

## Imp Note : I don't have the API_KEY of openAI therefore this code can't work