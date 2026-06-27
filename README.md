# README.md

```markdown
# Local LLM API

A lightweight REST API built with **FastAPI** that provides a clean interface for interacting with locally hosted Large Language Models (LLMs) through Ollama.

## Features

- RESTful API built with FastAPI
- Chat with any locally installed Ollama model
- Text generation endpoint
- List available local models
- Health check endpoint
- Automatic interactive API documentation
- Request validation using Pydantic

---

## Tech Stack

- Python
- FastAPI
- Ollama
- Pydantic
- Uvicorn

---

## Project Structure

```

.
├── server.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE

````

---

## Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/local-llm-api.git
cd local-llm-api
````

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Prerequisites

Install Ollama and ensure it is running locally.

Pull a model, for example:

```bash
ollama pull gemma:2b
```

Start the Ollama server

```bash
ollama serve
```

---

## Running the API

```bash
uvicorn server:app --reload
```

The API will be available at

```
http://127.0.0.1:8000
```

Interactive documentation

```
http://127.0.0.1:8000/docs
```

Alternative documentation

```
http://127.0.0.1:8000/redoc
```

---

## API Endpoints

| Method | Endpoint  | Description                  |
| ------ | --------- | ---------------------------- |
| GET    | /         | Welcome endpoint             |
| GET    | /health   | API health status            |
| GET    | /models   | List installed Ollama models |
| POST   | /chat     | Chat with a model            |
| POST   | /generate | Generate text                |

---

## Example Request

### Chat

POST `/chat`

```json
{
  "model": "gemma:2b",
  "message": "Explain recursion."
}
```

Example Response

```json
{
  "model": "gemma:2b",
  "response": "Recursion is..."
}
```

---

### Generate

POST `/generate`

```json
{
  "model": "gemma:2b",
  "prompt": "Write a short poem."
}
```

---

## Future Improvements

* Streaming responses
* Conversation memory
* Authentication
* Rate limiting
* Docker support
* Unit tests
* Logging
* Environment variable configuration

---

## License

This project is licensed under the MIT License.

```
```
