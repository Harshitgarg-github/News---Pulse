import feedparser

feed = feedparser.parse(
    "https://feeds.bbci.co.uk/news/rss.xml"
)

print("Latest BBC News:\n")

for article in feed.entries[:5]:
    print(article.title)