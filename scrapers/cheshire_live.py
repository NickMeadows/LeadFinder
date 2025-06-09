import feedparser
from datetime import datetime
from scrapers.base import BaseScraper

# Keyword categories for tagging and scoring
KEYWORDS = {
    "education": ["education", "college", "curriculum", "STEM", "learning", "university"],
    "skills": ["skills", "upskilling", "training", "apprenticeship", "vocational", "NVQ"],
    "funding": ["funding", "grant", "bid", "£", "million", "investment"],
    "partnerships": ["employer", "industry", "partner", "collaboration", "business"],
    "infrastructure": ["facility", "building", "digital", "equipment", "infrastructure"],
}

# Tag and score articles based on keyword matches
def tag_article(title, summary):
    tags = set()
    score = 0
    text = f"{title} {summary}".lower()
    for tag, words in KEYWORDS.items():
        if any(word in text for word in words):
            tags.add(tag)
            score += 1
    return list(tags), score

# Main scraper class
class CheshireLiveScraper(BaseScraper):
    @property
    def source(self):
        return "Cheshire Live (RSS)"

    def fetch(self):
        url = "https://www.cheshire-live.co.uk/news/?service=rss"
        feed = feedparser.parse(url)

        articles = []
        for entry in feed.entries:
            tags, score = tag_article(entry.title, entry.summary)

            articles.append({
                "title": entry.title,
                "url": entry.link,
                "summary": entry.summary,
                "source": self.source,
                "published_at": entry.published if "published" in entry else datetime.now().isoformat(),
                "tags": ",".join(tags),
                "notes": "",
                "relevance_score": score
            })

        return articles
