from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq( 
    model="llama-3.3-70b-versatile",   # https://console.groq.com/docs/models from here i can get the model
    temperature=0
)

prompt = PromptTemplate(
    template = "Give 5 points about this game {topic}",
    input_variables= ["topic"]
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"topic" : "cricket"})

print(result)

# chain.get_graph().print_ascii()     <-- this give the flow of the execution of the chain and for this i'll have install "grandalf"