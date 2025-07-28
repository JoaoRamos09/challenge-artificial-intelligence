from dotenv import load_dotenv
from app import create_app
import uvicorn
from app.backend.config.postgres_config import create_tables

load_dotenv()

if __name__ == "__main__":
    create_tables() 
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)