from pinecone import Pinecone
import os
from app.exception.pinecone_exception import PineconeIndexNotFound

def get_pc():
    return Pinecone(os.getenv("PINECONE_API_KEY"))

def get_index():
    pc = get_pc()
    try:
        index = pc.Index(os.getenv("PINECONE_INDEX_NAME"))
        return index
    except Exception as e:
        raise PineconeIndexNotFound(os.getenv("PINECONE_INDEX_NAME"))

