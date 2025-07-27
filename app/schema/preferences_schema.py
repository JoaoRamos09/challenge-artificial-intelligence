from sqlalchemy import Column, String, DateTime, Text, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
from app.enum.type_content_enum import TypeContentEnum
from app.enum.nivel_techinical_enum import NivelTechinicalEnum

Base = declarative_base()

class PreferencesSchema(Base):
    __tablename__ = "preferences"
    
    id = Column(String, primary_key=True)
    user_id = Column(String)
    level_technical = Column(Enum(NivelTechinicalEnum), nullable=False)
    preference_content = Column(Enum(TypeContentEnum), nullable=False)
    description = Column(Text)
    weaknesses = Column(Text)
    strengths = Column(Text)
    updated_at = Column(DateTime, default=datetime.now(datetime.UTC), onupdate=datetime.now(datetime.UTC))
    created_at = Column(DateTime, default=datetime.now(datetime.UTC))
