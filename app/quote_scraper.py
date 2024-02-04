from typing import Dict, List, Optional
import requests
from bs4 import BeautifulSoup


class QuoteScraper:
    def __init__(self) -> None:
        self.base_url = "https://quotes.toscrape.com"

    def get_html(self, url: str) -> str:
        response = requests.get(url)
        return response.text

    def clean_string(self, string: Optional[str]) -> Optional[str]:
        return string.strip() if string else None

    def scrape_text_and_author(self, tag: str) -> List[Dict[str, str]]:
        url = f"{self.base_url}/tag/{tag}/"
        html = self.get_html(url)

        soup = BeautifulSoup(html, "html.parser")
        quotes = soup.select(".quote")

        quotes_list: List[Dict[str, str]] = []

        for quote in quotes:
            text = quote.select_one("span.text").text
            author = quote.select_one("small.author").text

            _quote = {
                "text": self.clean_string(text),
                "author": self.clean_string(author),
            }
            print(_quote)
            quotes_list.append(_quote)

        return quotes_list


if __name__ == "__main__":
    quotes_scraper = QuoteScraper()
    quotes_scraper.scrape_text_and_author("life")
