import yaml
from application.scraper_service import ScraperService
from application.health_check_service import HealthCheckService

class WebScraper:
    def __init__(self, config_path):
        with open(config_path) as f:
            self.config = yaml.safe_load(f)
        self.health_checker = HealthCheckService()
        self.scraper = ScraperService()

    def scrape(self):
        results = []
        for site in self.config['sites']:
            is_healthy, response_time = self.health_checker.check(site['url'])
            if not is_healthy:
                print(f"Skipping {site['url']} due to health check failure")
                continue
            
            data = self.scraper.scrape_site(site['url'], site['selectors'])
            results.append(data)
        return results

if __name__ == "__main__":
    scraper = WebScraper("config.yaml")
    results = scraper.scrape()
    print("Scraping results:")
    for result in results:
        print(result)
