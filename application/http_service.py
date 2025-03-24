from fastapi import FastAPI
from scraper import WebScraper

class HttpService:
    def __init__(self, config_path, port=8000):
        self.app = FastAPI()
        self.port = port
        self.scraper = WebScraper(config_path)
        
        @self.app.get("/scrape")
        async def scrape():
            results = self.scraper.scrape()
            return {"results": results}

    def run(self):
        import uvicorn
        uvicorn.run(self.app, host="0.0.0.0", port=self.port)
