from fastapi import FastAPI
from pydantic import BaseModel
from ollama import Client
import ollama

app = FastAPI(
    title="Local LLM API",
    description="FastAPI wrapper for locally running Ollama models",
    version="1.0.0"
)

client = Client(host="http://localhost:11434")


# ---------- Request Models ----------

class ChatRequest(BaseModel):
    model: str
    message: str


class GenerateRequest(BaseModel):
    model: str
    prompt: str


# ---------- Routes ----------

@app.get("/")
def home():
    return {"message": "Welcome to Local LLM API"}


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_server": "connected"
    }


@app.get("/contact-us")
def contact_us():
    return {
        "email": "routalisha@331gmail.com"
    }


@app.get("/models")
def models():
    return ollama.list()


@app.post("/chat")
def chat(request: ChatRequest):

    response = client.chat(
        model=request.model,
        messages=[
            {
                "role": "user",
                "content": request.message
            }
        ]
    )

    return {
        "model": request.model,
        "response": response.message.content
    }


@app.post("/generate")
def generate(request: GenerateRequest):

    response = client.generate(
        model=request.model,
        prompt=request.prompt
    )

    return {
        "model": request.model,
        "response": response.response
    }