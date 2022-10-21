import asyncio
import configparser

from scrapy.crawler import CrawlerProcess
from twisted.internet import reactor
from twisted.internet.task import LoopingCall

from utils import print_info
from websites.facebook.facebook import Facebook
from websites.kijiji.kijiji import Kijiji


async def main(config):
    while True:
        print_info("Activating Scraper...")
        interval = config["DEFAULT"].getint("Interval")
        process_for_facebook = CrawlerProcess(settings={
            "FEEDS": {
                "items.json": {"format": "json"},
            },
            "LOG_ENABLED": False,
        })
        process = CrawlerProcess(settings={"FEEDS": {"items.json": {"format": "json", "overwrite": False}, }, "USER_AGENT": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36)', "LOG_ENABLED": False})
        if(config['FACEBOOK']['Enabled'] == 'True'):
            task = LoopingCall(lambda: process.crawl(Kijiji, config))
            task.start(60 * interval)
        
        reactor.run()
    


if __name__ == "__main__":
    print_info("Starting scraper")
    config = configparser.ConfigParser()
    config.read('config.ini')
    asyncio.run(main(config))
        
