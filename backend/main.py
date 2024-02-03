from fastapi import FastAPI

from dotenv import load_dotenv

import os

app = FastAPI()

load_dotenv()

from pymongo import MongoClient

client = MongoClient(os.getenv("MONGO_URI"))

@app.get("/")
def read_root():
    return {"Hello": "World"}

