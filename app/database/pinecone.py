from pinecone import Pinecone
import os

def get_pc():
    return Pinecone(os.getenv("PINECONE_API_KEY"))

def get_index():
    pc = get_pc()
    return pc.Index(os.getenv("PINECONE_INDEX_NAME"))

