#main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="LLM Service", version="0.1.0")

class GenerateRequest(BaseModel):
    prompt: str
    model: str = "gpt-4o"
    max_tokens: int = 100

@app.get("/")
async def root():
    return {"message": "Welcome to LLM Service!"}

@app.post("/generate")
async def generate(request: GenerateRequest):
    # Пока заглушка
    return {
        "status": "success",
        "response": f"LLM response for: {request.prompt[:50]}...",
        "model": request.model,
        "tokens_used": request.max_tokens
    }