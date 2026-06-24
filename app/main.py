from fastapi import FastAPI
from app.redis_client import r

app = FastAPI()

@app.get("/")
def root():
    return {
        "message":"DevOps Assignment API"
    }

@app.get("/health")
def health():

    try:
        r.ping()

        return {
            "status":"healthy",
            "redis":"connected"
        }

    except Exception:

        return {
            "status":"unhealthy"
        }

@app.get("/ai")
def ai(prompt:str):

    return {
        "prompt":prompt,
        "response":f"AI response for {prompt}"
    }