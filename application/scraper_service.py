from bs4 import BeautifulSoup
import requests

class ScraperService:
    def scrape_site(self, url, selectors):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = {}
        for key, selector in selectors.items():
            element = soup.select_one(selector)
            data[key] = element.text.strip() if element else None
        return data
