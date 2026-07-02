from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.password_service import analyze_password

app = FastAPI(
    title="Password Security Toolkit",
    version="1.0.0",
    description="API to analyze password security."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from models.request_models import PasswordRequest
from models.response_models import PasswordAnalysisResponse

@app.get("/")
def home():
    return {
        "message": "Welcome to Password Security Toolkit!"
    }

@app.post("/analyze-password", response_model=PasswordAnalysisResponse)
def analyze(request: PasswordRequest):
    return analyze_password(request.password)