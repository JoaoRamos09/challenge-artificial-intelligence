from sqlalchemy import create_engine
import os
from sqlalchemy.ext.declarative import declarative_base
from app.backend.schema.conversation_schema import ConversationSchema
from app.backend.schema.message_schema import MessageSchema
from app.backend.schema.preference_schema import PreferenceSchema
from app.backend.database.base import Base

def create_tables():
    
    database_url = os.getenv("DATABASE_URL")
    engine = create_engine(database_url)
    Base.metadata.create_all(bind=engine)

def get_base():
    return Base

if __name__ == "__main__":
    create_tables()

