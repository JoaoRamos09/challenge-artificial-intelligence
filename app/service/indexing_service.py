
from pinecone import Pinecone
from app.dto.chunk_dto import ChunkDTO
import os
import json
from app.exception.pinecone_exception import PineconeUpsertError
from app.database.pinecone import get_index

class IndexingService:
    def __init__(self):
        self.index = get_index()
        self.namespace = os.environ.get("PINECONE_NAMESPACE")

    def save_data(self, chunks:list[ChunkDTO]):
        formatted_data = [self.format_data_dict(chunk) for chunk in chunks]
        try:
            self.index.upsert_records(self.namespace,formatted_data)
        except Exception as e:
            print(e)
            raise PineconeUpsertError(self.namespace, self.index.name)
    
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
        
        
        
