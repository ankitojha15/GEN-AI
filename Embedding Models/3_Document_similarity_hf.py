from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

Documents = [ 
    "Virat kohli is the bets player in the world",
    "Jasprit Bumrah is the best bowler in the world",
    "Sachin tendulkar is a class player",
    "Ms Dhoni is the best captain"
]

query = "Tell me about virat"

doc_embeddings = embeddings.embed_documents(Documents)
query_embedding = embeddings.embed_query(query)

score = cosine_similarity([query_embedding],doc_embeddings)[0] # This [0] give 1D list out of 2D list and both of 
                            #them needs to be 2d and final result should be 1d and that is wherre the [0] comes in

index , score = sorted(list(enumerate(score)),key=lambda x:x[1])[-1]

print(query)
print(Documents[index])
print("The score b/w query and Documents is: ", score)
