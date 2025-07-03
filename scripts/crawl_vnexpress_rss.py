import feedparser
import psycopg2
from datetime import datetime

# Config Postgres connection
DB_CONFIG = {
    "dbname": "news_db",
    "user": "postgres",
    "password": "yourpassword",
    "host": "postgres",  # dùng service name trong docker-compose
    "port": "5432"
}

# List of RSS feeds (multi-category)
RSS_FEEDS = [
    "https://vnexpress.net/rss/thoi-su.rss",
    "https://vnexpress.net/rss/the-gioi.rss",
    "https://vnexpress.net/rss/kinh-doanh.rss",
    "https://vnexpress.net/rss/giai-tri.rss",
    "https://vnexpress.net/rss/the-thao.rss",
    # ... thêm các URL khác theo nhu cầu
]

def save_to_db(entries):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    for entry in entries:
        cur.execute("""
            INSERT INTO news_articles (title, summary, link, publish_date)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (link) DO NOTHING;
        """, (
            entry.get("title"),
            entry.get("summary"),
            entry.get("link"),
            datetime(*entry.published_parsed[:6]) if hasattr(entry, "published_parsed") else None
        ))
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    all_entries = []
    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        all_entries.extend(feed.entries)
    save_to_db(all_entries)
    print(f"Inserted {len(all_entries)} articles.")
