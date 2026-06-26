import feedparser

feeds = {
    "BBC": "https://feeds.bbci.co.uk/news/rss.xml",
    "NPR": "https://feeds.npr.org/1001/rss.xml",
    "Guardian": "https://www.theguardian.com/world/rss"
}

all_articles = []

for source, url in feeds.items():

    feed = feedparser.parse(url)

    for article in feed.entries[:5]:

        article_data = {
            "source": source,
            "title": article.title,
            "link": article.link,
            "published": article.get("published", "No Date")
        }

        all_articles.append(article_data)

print(f"\nTotal Articles: {len(all_articles)}\n")

for article in all_articles[:3]:
    print(article)