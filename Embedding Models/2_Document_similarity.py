from langchain_openAI import openAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 

load_dotenv()

embeddings = openAIEmbeddings(model = 'text-embedding-3-large', dimension = 300)

documents = (
    "Virat kohli is the bets player in the world",
    "Jasprit Bumrah is the best bowler in the world",
    "Sachin tendulkar is a class player",
    "Ms Dhoni is the best captain"
    )

query = "Tell me about kohli"

query_embedding = embedding.embed_query(query)
doc_embeddings = embedding.embed_documents(documents)

scores = cosine_similarity([query_embedding], doc_embeddings)[0] ## for simmilarity always send 2d list

index , score = sorted((list(enumerate(scores))),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("The similarity b/w query and document is: "score)  ## score is the similarity between query and document



