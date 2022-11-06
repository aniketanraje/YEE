import requests 
from zipfile import ZipFile
import os

class ZipDownloader:
    
    
    def __init__(self,download_url):
        self.download_url = download_url


    def zip_downloader(self):
        dir_path = "./../data/"
        print(self.download_url)
        file_name = self.download_url.split("/")[-1]
        file_name = dir_path + file_name
        print("Download URL is: \t",self.download_url)
        download = requests.get(self.download_url)
        if download.status_code == 200:
            with open(file_name, "wb") as file_handler:
                file_handler.write(download.content)
                print(os.getcwd())
            print("Calling zip extractor")
            self.zip_extractor(file_name)


    def zip_extractor(self,file_name):
        print("\n file_name:\t",file_name)
        z= "./../data/" + (file_name.split("/")[-1]).split(".")[0]
        with ZipFile(file_name,"r") as f: 
            f.extractall(z)

