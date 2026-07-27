from langchain_core.prompts import MessagesPlaceholder,ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model = "llama-3.3-70b-versatile"
)
chat_template = ChatPromptTemplate([
    ('system','you are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []

with open("4.Prompts/chat_history.txt") as f:
    chat_history.extend(f.readlines())

print(chat_history)

prompt = chat_template.invoke({'chat_history':chat_history,'query':'Where is my refund'})

result = model.invoke(prompt)

print(result.content)