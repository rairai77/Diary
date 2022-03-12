import uvicorn
from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from os.path import join, dirname

load_dotenv(join(dirname(__file__), '.env'))

client = MongoClient(os.environ.get('LINK'))
db = client["diaryDB"]
entries = db["entries"]
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.on_event("shutdown")
def shutdown_event():
    client.close()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
