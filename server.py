from fastapi import FastAPI
from pydantic import BaseModel
from ollama import Client
import ollama
import logging

# ---------------- Logging Setup ----------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("local-llm-api")

# ---------------- FastAPI App ----------------
app = FastAPI(
    title="Local LLM API",
    description="A FastAPI wrapper for locally running Ollama models",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# ---------------- Ollama Client ----------------
client = Client(host="http://localhost:11434")


# ---------------- Request Models ----------------
class ChatRequest(BaseModel):
    model: str
    message: str


class GenerateRequest(BaseModel):
    model: str
    prompt: str


# ---------------- Routes ----------------

@app.get("/")
def home():
    return {
        "message": "Welcome to Local LLM API",
        "docs": "/docs"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "FastAPI",
        "model_server": "Ollama running at localhost:11434"
    }


@app.get("/models")
def models():
    try:
        data = ollama.list()

        model_names = [
            model.get("name", "unknown")
            for model in data.get("models", [])
        ]

        return {
            "models": model_names
        }

    except Exception as e:
        logger.error(f"Error fetching models: {str(e)}")
        return {
            "error": "Failed to fetch models"
        }


@app.post("/chat")
def chat(request: ChatRequest):

    try:
        logger.info(
            f"Chat request | model={request.model} | message_length={len(request.message)}"
        )

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

    except Exception as e:
        logger.error(f"Chat error: {str(e)}")
        return {
            "error": str(e)
        }


@app.post("/generate")
def generate(request: GenerateRequest):

    try:
        logger.info(
            f"Generate request | model={request.model} | prompt_length={len(request.prompt)}"
        )

        response = client.generate(
            model=request.model,
            prompt=request.prompt
        )

        return {
            "model": request.model,
            "response": response.response
        }

    except Exception as e:
        logger.error(f"Generate error: {str(e)}")
        return {
            "error": str(e)
        }
        logger.error(f"Generate error: {str(e)}")
        return {"error": str(e)}
