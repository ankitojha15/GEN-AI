from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

documents = ("Delhi is the capital of India",
"India is a country in Asia",
"Asia is a continent")

vector = embeddings.embed_documents(documents)

print(str(vector))

