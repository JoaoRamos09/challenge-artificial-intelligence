from pydantic import BaseModel, Field

class PDFAnalysisDTO(BaseModel):
    tags: list[str] = Field(description="As principais palavras chaves do PDF")
    subject: str = Field(description="Assunto do PDF")
    technical_level: str = Field(description="Nível técnico do PDF")