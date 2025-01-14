import asyncio
from gauguin import GauguinScraper

if __name__ == "__main__":
    scraper = GauguinScraper()
    asyncio.run(scraper.scrape())