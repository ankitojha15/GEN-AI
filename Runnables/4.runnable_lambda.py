from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence ,RunnableParallel,RunnablePassthrough ,RunnableLambda
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

def word_count(text):
    return len(text.split())

parser = StrOutputParser()

runnableword_count = RunnableLambda(word_count)

joke_gen_chain = RunnableSequence(prompt,model,parser)

parellel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "wordcount":RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_gen_chain,parellel_chain)

result = final_chain.invoke({"topic":"AI"})

final_result = """{} \n word count - {}""".format(result["joke"],result["wordcount"])

print(final_result)