import os
import sys

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from app.db import get_db
from scrapers.cheshire_live import CheshireLiveScraper

def ingest_articles(articles):
    db = get_db()
    for article in articles:
        exists = db.execute("SELECT 1 FROM articles WHERE url = ?", (article['url'],)).fetchone()
        if not exists:
            db.execute("""
                INSERT INTO articles (title, url, summary, source, published_at, tags, relevance_score, notes)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                article["title"],
                article["url"],
                article["summary"],
                article["source"],
                article["published_at"],
                article["tags"],
                article["relevance_score"],
                article["notes"]
            ))
    db.commit()

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        scraper = CheshireLiveScraper()
        articles = scraper.fetch()
        ingest_articles(articles)
        print(f"✅ Ingested {len(articles)} articles.")
