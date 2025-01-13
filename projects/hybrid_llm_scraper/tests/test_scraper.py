from src.scraper.base import BaseScraper

def test_base_scraper():
    scraper = BaseScraper()
    assert scraper.name == "base_scraper"
