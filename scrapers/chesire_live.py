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

        for item in soup.select("div.teaser"):
            title_el = item.select_one("h3.teaser__headline")
            link_el = item.select_one("a")
            summary_el = item.select_one("p")

            if title_el and link_el:
                title = title_el.get_text(strip=True)
                link = link_el["href"]
                summary = summary_el.get_text(strip=True) if summary_el else ""

                # Ensure absolute URLs
                if link.startswith("/"):
                    link = "https://www.cheshire-live.co.uk" + link

                articles.append({
                    "title": title,
                    "url": link,
                    "summary": summary,
                    "source": self.source,
                    "published_at": datetime.now().isoformat(),
                    "tags": "",
                    "notes": ""
                })

        return articles
