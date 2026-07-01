from fastapi import FastAPI
from pydantic import BaseModel
from services.password_service import analyze_password

app = FastAPI(
    title="Password Security Toolkit",
    version="1.0.0",
    description="API to analyze password security."
)

class PasswordRequest(BaseModel):
    password: str

@app.get("/")
def home():
    return {
        "message": "Welcome to Password Security Toolkit!"
    }

@app.post("/analyze-password")
def analyze(request: PasswordRequest):
    return analyze_password(request.password)