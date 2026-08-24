from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence , RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature= 1.9,

)

prompt1 = PromptTemplate(
    template= "Generate a tweet about {topic}",
    input_variables=['topic']
)


prompt2 = PromptTemplate(
    template='Generate a Linkedin post about {topic}', 
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = RunnableParallel({
    "tweet":RunnableSequence(prompt1,model , parser),
    "linkedin": RunnableSequence(prompt2,model,parser)
})

# Note: We use dict in RParelle.
result  = chain.invoke({"topic":"AI"})

print("Tweet",result['tweet'])
print("===="*40)
print("Linedin",result["linkedin"])