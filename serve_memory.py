from fastapi import FastAPI
from pydantic import BaseModel
import subprocess

app = FastAPI()

class Query(BaseModel):
    text: str

@app.post("/api/memory/search")
def search_memory(query: Query):
    # Calls basic-memory locally on the Lenovo
    result = subprocess.run(
        ["basic-memory", "search", query.text, "--project", "second-brain"],
        capture_output=True, text=True
    )
    return {"context": result.stdout}

@app.get("/health")
def health():
    return {"status": "Second Brain Online"}
