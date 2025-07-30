
from pinecone import Pinecone
from app.backend.dto.chunk_dto import ChunkDTO
import os
from app.backend.exception.pinecone_exception import PineconeUpsertError, PineconeRetrieveError
from app.backend.database.pinecone import get_index
import logging


class IndexingService:
    def __init__(self):
        self.index = get_index()
        self.index_name = os.environ.get("PINECONE_INDEX_NAME")

    def save_data(self, chunks:list[ChunkDTO]):
        logging.info(f"[INDEXING SERVICE] Save data in: {os.getenv('NAMESPACE_DEV')}")
        formatted_data = [self.format_data_dict(chunk) for chunk in chunks]
        try:
            self.index.upsert_records(os.getenv("NAMESPACE_DEV"),formatted_data)
        except Exception as e:
            print(e)
            raise PineconeUpsertError(os.getenv("NAMESPACE_DEV"), self.index_name)
    
    def format_data_dict(self, chunk:ChunkDTO):
        data_dict = {
            "id": chunk.id,
            "data": chunk.content if chunk.content else "",
            "tags": chunk.tags if chunk.tags else [],
            "path": chunk.path if chunk.path else "",
            "type_file": chunk.type_file.value if chunk.type_file else ""
        }
        
        if chunk.metadata:
            for key, value in chunk.metadata.items():
                data_dict[key] = str(value)
        
        return data_dict
    
    def retrieve_data(self, query: str):
        try:
            chunks = self.index.search(
                namespace=os.getenv("NAMESPACE_PROD"),
                query={
                    "top_k": 5,
                    "filter": {
                        "tags": {"$in": ["HTML", "HTML5", "CSS"]}
                    },
                    "inputs": {
                        "text": query
                    }
                }
            )
            return [str(hit["fields"]["data"]) for hit in chunks["result"]["hits"]]
        
        except Exception as e:
            print(e.message)
            raise PineconeRetrieveError(os.getenv("NAMESPACE_DEV"), self.index_name)
        
        
        
