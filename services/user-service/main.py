from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/users")
def get_users():
    return {
        "users": ["alice", "bob"],
        "db_password": os.getenv("DB_PASSWORD", "not-set")
    }

@app.get("/health")
def health():
    return {"status": "ok"}
