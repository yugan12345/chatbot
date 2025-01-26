from embeddings import CodeBERTEmbedder
from vectorstore import VectorStore
from retriever import RAGRetriever
from chatbot import CPChatbot
import numpy as np
import torch

# Path to folder containing text files with solutions
folder_path = r"D:\Games\src\data\editorials"

# Initialize components
embedder = CodeBERTEmbedder()
vector_store = VectorStore(dimension=768)  # Adjust dimension based on your model
retriever = RAGRetriever(embedder, vector_store)

# Generate and store embeddings with chunks
print("Generating embeddings from solution files...")
embeddings, chunks = embedder.generate_embeddings_from_folder(folder_path)
if isinstance(embeddings, torch.Tensor):
    embeddings = [embeddings]
embeddings_array = torch.stack(embeddings).numpy()

# Add embeddings and their corresponding chunks to the vector store
vector_store.add_vectors(embeddings_array, chunks)
print(f"Stored {len(embeddings)} embeddings in the vector store.")

# Create chatbot
system_message = """I am solving a Competitive Programming problem, and I need help understanding its solution."""
chatbot = CPChatbot(retriever, system_message)

# Query the chatbot
query = "How can I solve 1857 C?"
response = chatbot.chat(query)
print(response)
