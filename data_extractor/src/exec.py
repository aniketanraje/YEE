from crawler import Crawler
from scrapper import Scrapper
from downloader import ZipDownloader


crawl_urls = ["https://genderdata.worldbank.org/topics/employment-and-time-use/",
"https://genderdata.worldbank.org/topics/education/",
"https://genderdata.worldbank.org/topics/youth-15-24/"]

for crawl_url in crawl_urls:
    print("crawl url: ", crawl_url)
    print("Calling Crawler")
    crawler = Crawler(crawl_url)
    print("Calling scrapper")
    scrapper = Scrapper(crawler.url, crawler.response)
    print("Calling downloader")
    downloader = ZipDownloader(scrapper.get_download_link())
    downloader.zip_downloader()
    print("downloaded dataset:",crawl_url.split("/")[-2])