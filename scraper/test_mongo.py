from pymongo import MongoClient

MONGO_URI = "mongodb+srv://harshitgarg9870_db_user:YOUR_PASSWORD@cluster0.am8ftpg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URI)

db = client["news_pulse"]

print("MongoDB Connected Successfully!")