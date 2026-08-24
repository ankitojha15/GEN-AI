from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence , RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature= 1.9,

)

pass_through = RunnablePassthrough()

print(pass_through.invoke("Runnable Passthrough gives the same output as whateven is provided in Input"))

# Runnable Passthrough give the same output as whateven is provided in Input
