from fastapi import FastAPI, Depends
from .quote_scraper import QuoteScraper


app = FastAPI()
quote_scraper = QuoteScraper()


@app.get("/quotes/{tag}")
async def quotes(tag: str = "love", quote_scraper: QuoteScraper = Depends()):
    data = quote_scraper.scrape_text_and_author(tag)
    return data
