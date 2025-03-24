import requests
import time

class HealthCheckService:
    def check(self, url, timeout=5, retries=3):
        for attempt in range(retries):
            try:
                start_time = time.time()
                response = requests.head(url, timeout=timeout)
                response_time = time.time() - start_time
                
                if response.status_code == 200:
                    return True, response_time
                
                print(f"Health check failed for {url}: Status {response.status_code} (Attempt {attempt + 1}/{retries})")
            except requests.RequestException as e:
                print(f"Health check error for {url}: {str(e)} (Attempt {attempt + 1}/{retries})")
            
            if attempt < retries - 1:
                time.sleep(1)
        
        return False, None
