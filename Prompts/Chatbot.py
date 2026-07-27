from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

load_dotenv() 

model = ChatGroq(
    model="llama-3.3-70b-versatile",   # https://console.groq.com/docs/models from here i can get the model
    temperature=0.1
)

chat_history = [
    SystemMessage(content = "You are a helpful AI assistant")
]

while True:
    user_input = input("user : ")
    chat_history.append(HumanMessage(content = user_input))
    if user_input == 'exit':
        break
    else:
        result = model.invoke(chat_history)
        chat_history.append(AIMessage(content = result.content))
        print("AI : ",result.content)

print(chat_history)