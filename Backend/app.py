from fastapi import FastAPI

from services.password_service import analyze_password

app = FastAPI(
    title="Password Security Toolkit",
    version="1.0.0",
    description="API to analyze password security."
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