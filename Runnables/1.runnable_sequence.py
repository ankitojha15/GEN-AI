from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature= 1.9,

)

prompt = PromptTemplate(
    template = """ write a Joke about 
    Do NOT use Markdown.
    Do NOT use **bold**.
    Return plain text only.
    {topic}""",
    input_variables= ["topic"],
    
)

prompt2 = PromptTemplate(
    template = """ Exaplain the following. 
    Do NOT use Markdown.
    Do NOT use **bold**.
    Return plain text only.
    {text}""",
    input_variables= ["text"],
    
)

model = model

parser = StrOutputParser()

chain = RunnableSequence(prompt , model , parser , prompt2 , model , parser)

print(chain.invoke({"topic": "AI"}))