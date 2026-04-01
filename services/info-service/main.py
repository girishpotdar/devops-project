
from fastapi import FastAPI
import socket
import os

app = FastAPI()

@app.get("/info")
def info():
    return {
            "service": "info-service",
            "hostname": socket.gethostname(),
            "env": os.getenv("ENV", "dev")
    }


@app.get("/health")
def health():
    return {"status": "ok"}



