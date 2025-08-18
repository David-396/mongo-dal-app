from fastapi import FastAPI
from pymongo import MongoClient
import os
from starlette.responses import JSONResponse

app = FastAPI()

MONGO_HOST = os.getenv("MONGO_HOST", "mongodb")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_USER = os.getenv("MONGO_USER", "root")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "pass")

client = MongoClient(
    host=MONGO_HOST,
    port=MONGO_PORT,
    username=MONGO_USER,
    password=MONGO_PASSWORD
)

db = client[os.environ.get('MONGODB_DB_NAME', "mongoDB_DAL_DB")]
collection = db[os.environ.get('MONGODB_COLLECTION_NAME', "project_collection")]

@app.get('/get-data')
def get_data():
    try:
        data = collection.find({})
        return JSONResponse(data)
    except Exception as e:
        print(e)
