from scrapers.base import BaseScraper
import requests
from bs4 import BeautifulSoup
from datetime import datetime

class CheshireLiveScraper(BaseScraper):
    @property
    def source(self):
        return "Cheshire Live"

    def fetch(self):
        url = "https://www.cheshire-live.co.uk/news/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        articles = []
        for item in soup.select("div.teaser"):  # Selector may need refining
            title = item.select_one("h3")
            link = item.select_one("a")
            summary = item.select_one("p")

            if title and link:
                articles.append({
                    "title": title.get_text(strip=True),
                    "url": link["href"],
                    "summary": summary.get_text(strip=True) if summary else "",
                    "source": self.source,
                    "published_at": datetime.now().isoformat(),
                    "tags": "",
                    "notes": ""
                })
        return articles
