from fastapi import FastAPI

import os

app = FastAPI()

from pymongo import MongoClient

client = MongoClient(os.getenv("MONGO_URI"))

@app.get("/")
def read_root():
    return {"Hello": "World"}

