from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence ,RunnableParallel,RunnablePassthrough ,RunnableLambda , RunnableBranch
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature= 1.9,

)

prompt1 = PromptTemplate(
    template= "write a detailed report on {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template= "summarize the follwoing text \n {text}",
    input_variables= ["text"]
)

parser = StrOutputParser()

report_gen_chain = prompt1 | model | parser # Runnablesequence as LCEL


branch_chain = RunnableBranch(
    (lambda x:len(x.split())>100,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain = report_gen_chain | branch_chain

print(final_chain.invoke({"topic":"Russia vs Ukrain"}))






# kind of conditional chain
# we send tuples in it as per conditions and within it we write (condition,runnable)