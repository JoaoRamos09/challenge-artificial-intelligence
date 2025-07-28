from sqlalchemy import create_engine
import os
from sqlalchemy.ext.declarative import declarative_base
from app.schema.conversation_schema import ConversationSchema
from app.schema.message_schema import MessageSchema
from app.schema.preference_schema import PreferenceSchema
from app.database.base import Base

def create_tables():
    
    database_url = os.getenv("DATABASE_URL")
    engine = create_engine(database_url)
    Base.metadata.create_all(bind=engine)

def get_base():
    return Base

if __name__ == "__main__":
    create_tables()

