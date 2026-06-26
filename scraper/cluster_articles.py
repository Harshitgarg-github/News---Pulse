from pymongo import MongoClient
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

MONGO_URI = "mongodb+srv://harshitgarg9870_db_user:NewPulse9492@cluster0.am8ftpg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


client = MongoClient(MONGO_URI)

db = client["news_pulse"]
collection = db["articles"]

articles = list(collection.find())

titles = [article["title"] for article in articles]

vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(titles)

kmeans = KMeans(n_clusters=3, random_state=42)

kmeans.fit(X)

for i, article in enumerate(articles):

    cluster_id = int(kmeans.labels_[i])

    collection.update_one(
        {"_id": article["_id"]},
        {"$set": {"cluster_id": cluster_id}}
    )

    print(
        article["title"],
        "-> Cluster",
        cluster_id
    )

print("\nClustering Completed!")