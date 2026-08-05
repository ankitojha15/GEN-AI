from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal 

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

class Feedback(BaseModel):
    sentiment: Literal['Negative','Positive'] = Field(description="Give the sentiment of the feedback")

parser = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Feedback)


class Feedback(BaseModel):
    sentiment: Literal['Negative','Positive'] = Field(description="Give the sentiment of the feedback")

prompts = PromptTemplate(
    template = "classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instructions}",
    input_variables= ["feedback"],
    partial_variables={"format_instructions":parser2.get_format_instructions()}
)


classifier_chain = prompts | model | parser2

prompt2 = PromptTemplate(
template='Write an appropriate response to this positive feedback \n {feedback}',
input_variables=[' feedback' ]
)

prompt3 = PromptTemplate(
template='Write an appropriate response to this negative feedback \n {feedback}', 
input_variables=["feedback"]
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == "Positive",prompt2 | model | parser),
    (lambda x:x.sentiment == "Negative",prompt3 | model | parser),
    RunnableLambda(lambda x : "cound not find sentiment") 
)

chain = classifier_chain | branch_chain

result = chain.invoke({"feedback":"This phone is terrible"})
print(result)

