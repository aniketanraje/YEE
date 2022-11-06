from crawler import Crawler
from scrapper import Scrapper
from downloader import ZipDownloader

crawl_url = input("Input source url:\t")
print("Calling Crawler")
crawler = Crawler(crawl_url)
print("Calling scrapper")
scrapper = Scrapper(crawler.url, crawler.response)
print("Calling downloader")
downloader = ZipDownloader(scrapper.get_download_link())
downloader.zip_downloader()