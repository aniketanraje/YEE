from downloader import ZipDownloader

downloader = ZipDownloader(None)

print("calling extractor")
downloader.zip_extractor("./../data/education.zip")
