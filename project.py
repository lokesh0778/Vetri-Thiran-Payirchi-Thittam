from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(
    title="ComicCraft - AI Comic Story Creator",
    description="Create AI-powered comic stories using Gemini models",
    version="1.0.0"
)

# Allow frontend to connect with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "ComicCraft API is running!",
        "status": "success"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/api/test")
def test_api():
    return {
        "message": "Backend connection successful!"
    }