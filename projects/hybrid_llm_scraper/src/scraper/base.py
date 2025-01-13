class BaseScraper:
    """Base class for all scrapers"""
    def __init__(self):
        self.name = "base_scraper"

    def scrape(self):
        raise NotImplementedError 