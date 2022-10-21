import configparser

from scrapy.crawler import CrawlerProcess

from websites.facebook.facebook import Facebook


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    process = CrawlerProcess(settings={
        "FEEDS": {
            "items.json": {"format": "json"},
        },
    })
    process.crawl(Facebook, config=config)
    process.start()


if __name__ == "__main__":
    main()
