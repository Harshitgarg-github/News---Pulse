from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# ===========================
# Load Environment Variables
# ===========================
load_dotenv()

# ===========================
# FastAPI App
# ===========================
app = FastAPI()

# ===========================
# CORS Configuration
# ===========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Production me specific domain use karna
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===========================
# MongoDB Connection
# ===========================
MONGO_URI = os.getenv("MONGO_URI")

collection = None

try:
    if not MONGO_URI:
        raise Exception("MONGO_URI not found in .env file")

    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    client.server_info()  # Test connection

    db = client["news_pulse"]
    collection = db["articles"]

    print("✅ MongoDB Connected Successfully")

except Exception as e:
    print("❌ MongoDB Connection Failed")
    print(e)

# ===========================
# Home Route
# ===========================
@app.get("/")
def home():
    return {
        "message": "News Pulse API is Running 🚀"
    }

# ===========================
# Cluster Route
# ===========================
@app.get("/clusters")
def get_clusters():

    if collection is None:
        return {
            "status": "error",
            "message": "Database not connected"
        }

    articles = list(collection.find({}, {"_id": 0}))

    clusters = {}

    for article in articles:

        cluster_id = str(article.get("cluster_id", 0))

        if cluster_id not in clusters:
            clusters[cluster_id] = []

        clusters[cluster_id].append({
            "title": article.get("title"),
            "source": article.get("source"),
            "cluster_id": article.get("cluster_id")
        })

    return clusters