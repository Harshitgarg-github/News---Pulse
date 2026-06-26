import feedparser
from pymongo import MongoClient

MONGO_URI = "mongodb+srv://harshitgarg9870_db_user:NewPulse9870@cluster0.am8ftpg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


client = MongoClient(MONGO_URI)

db = client["news_pulse"]

collection = db["articles"]

print("Testing MongoDB...")

try:
    client.admin.command("ping")
    print("MongoDB Ping Successful")
except Exception as e:
    print("MongoDB Error:", e)
    exit()

feeds = {
    "BBC": "https://feeds.bbci.co.uk/news/rss.xml",
    "NPR": "https://feeds.npr.org/1001/rss.xml",
    "Guardian": "https://www.theguardian.com/world/rss"
}

count = 0

for source, url in feeds.items():

    feed = feedparser.parse(url)

    for article in feed.entries[:5]:

        article_data = {
            "source": source,
            "title": article.title,
            "link": article.link,
            "published": article.get("published", "")
        }

        existing = collection.find_one({"link": article.link})

if not existing:
    collection.insert_one(article_data)
    count += 1


print(f"{count} Articles Saved Successfully")