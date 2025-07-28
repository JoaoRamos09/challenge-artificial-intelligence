from sqlalchemy import Column, Integer, DateTime, Text, Enum
from datetime import datetime
from app.backend.enum.type_content_enum import TypeContentEnum
from app.backend.enum.nivel_techinical_enum import NivelTechinicalEnum
from app.backend.database.base import Base

class PreferenceSchema(Base):
    __tablename__ = "preferences"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    level_technical = Column(Enum(NivelTechinicalEnum), nullable=False)
    preference_content = Column(Enum(TypeContentEnum), nullable=False)
    description = Column(Text)
    weaknesses = Column(Text)
    strengths = Column(Text)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    created_at = Column(DateTime, default=datetime.now())
