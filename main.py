from dotenv import load_dotenv
from app import create_app
import uvicorn

load_dotenv()
app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)