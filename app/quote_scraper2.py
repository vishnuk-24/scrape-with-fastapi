from typing import Dict, List, Optional

import requests_html


class Quote2Scraper:
    def __init__(self) -> None:
        self.session = requests_html.HTMLSession()

    def get_html(self, url: str) -> requests_html.HTML:
        response = self.session.get(url)
        return response.html

    @staticmethod
    def clean_string(string: Optional[str]) -> Optional[str]:
        return string.strip() if string else None

    def scrape_text_and_author(self, tag: str) -> List[Dict[str, str]]:
        base_url = "https://quotes.toscrape.com/tag/"
        url = f"{base_url}{tag}/"
        html = self.get_html(url)

        quotes = html.find("div.quote")
        quotes_list: List[Dict[str, str]] = []

        for quote in quotes:
            text = quote.find("span.text", first=True).text
            author = quote.find("small.author", first=True).text

            _quote = {
                "text": self.clean_string(text),
                "author": self.clean_string(author),
            }

            print(_quote)
            quotes_list.append(_quote)

        return quotes_list


if __name__ == "__main__":
    quotes_scraper = Quote2Scraper()
    quotes_scraper.scrape_text_and_author("life")
