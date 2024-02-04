from fastapi import FastAPI, Depends
from .quote_scraper import QuoteScraper
from .quote_scraper2 import Quote2Scraper


app = FastAPI()
quote_scraper = QuoteScraper()
quote_scraper2 = Quote2Scraper()


@app.get("/quotes/{tag}")
async def quotes(tag: str = "love", quote_scraper: QuoteScraper = Depends()):
    data = quote_scraper.scrape_text_and_author(tag)
    return data

@app.get("/quotes2/{tag}")
async def quotes(tag: str = "love", quote_scraper2: Scraper = Depends()):
    return quote_scraper2.scrape_text_and_author(tag)
