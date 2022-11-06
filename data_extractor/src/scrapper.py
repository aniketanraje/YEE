from bs4 import BeautifulSoup

class Scrapper:
    
    
    def __init__(self,url, response):
        self.url = url 
        self.response = response 
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        self.head_url = "https://genderdata.worldbank.org"


    def get_download_link(self):
        links = []
        for link in self.soup.find_all("a"):
            if link.string == "CSV":
                self.tail_url = link.get("href")  
                return self.head_url + self.tail_url

        
