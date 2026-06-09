from fastapi import FastAPI

app = FastAPI(title="Am I Cooked? API")

@app.get("/")
def welcome():
    return {"message": "Welcome to the Am I cooked? API", "docs": "/docs"}

