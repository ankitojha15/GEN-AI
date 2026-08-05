from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq( 
    model="llama-3.3-70b-versatile",   # https://console.groq.com/docs/models from here i can get the model
)

prompt1 = PromptTemplate(
    template = "Generate a detailed report on \n {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = """"
Generate a 5-point summary of the following text.

Do NOT use Markdown.
Do NOT use **bold**.
Return plain text only.

{text}
""",
    input_variables=["text"]
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic":"cricket"})

print(result)