""" RunnableLambda : 
RunnableLambda is a runnable primitive that allows you to apply custom Python functions within an Al pipeline.
It acts as a middleware between different Al components, enabling preprocessing, transformation, API calls, filtering, and post-processing in a LangChain workflow."""

from langchain_core.runnables import RunnableLambda

def word_count(text):
    return len(text.split())

runnableword_count = RunnableLambda(word_count)

print(runnableword_count.invoke("Hii, How are you?"))


