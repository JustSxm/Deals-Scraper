import configparser
from twisted.internet.task import LoopingCall
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from websites.amazon import Amazon
from websites.ebay import Ebay
from websites.facebook import Facebook
from websites.kijiji import Kijiji
from websites.lespacs import Lespacs


def main():
    config = configparser.ConfigParser(allow_no_value=False)
    if(len(config.read('config.ini')) < 1):
        create_config(config)
    config.read('config.ini')
    keywords = config['DEFAULT']['Keywords']
    keywords = keywords.split(",")
    exclusions = config['DEFAULT']['Exclusions']
    exclusions = exclusions.split(",")
    max_price = config['DEFAULT']['MaxPrice']
    min_price = config['DEFAULT']['MinPrice']
    enable_facebook = config['DEFAULT'].getboolean('EnableFacebook')
    enable_kijiji = config['DEFAULT'].getboolean('EnableKijiji')
    enable_ebay = config['DEFAULT'].getboolean('EnableEbay')
    enable_amazon = config['DEFAULT'].getboolean('EnableAmazon')
    enable_lespacs = config['DEFAULT'].getboolean('EnableLespacs')
    strictmode = config['DEFAULT'].getboolean('StrictMode')
    facebook_city_id = config['DEFAULT']['FacebookCityId']
    interval = config['DEFAULT']['Interval']
    if(enable_facebook):
        scrape(Facebook, keywords, exclusions,
               max_price, min_price, interval, strictmode, facebook_city_id)
    if(enable_kijiji):
        scrape(Kijiji, keywords,
               exclusions, max_price, interval, min_price, strictmode)
    if(enable_ebay):
        scrape(Ebay, keywords, exclusions, interval,
               max_price, min_price, strictmode)
    if(enable_amazon):
        scrape(Amazon, keywords,
               exclusions, max_price, interval, min_price, strictmode)
    if(enable_lespacs):
        scrape(Lespacs, keywords,
               exclusions, max_price, interval, min_price, strictmode)
    reactor.run()


process = CrawlerRunner(
    settings={"FEEDS": {"hits.json": {"format": "json", "overwrite": False}, }, "USER_AGENT": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36)'})  # Kijiji has anti scraping method using the user agent


def scrape(spider, keywords: list, exclusions: list, max_price, min_price, interval, strictmode, facebook_city_id=None):
    if(facebook_city_id):
        # Facebook behaves differently with another user agent
        process_for_facebook = CrawlerRunner(
            settings={"FEEDS": {"hits.json": {"format": "json", "overwrite": False}}})
        task = LoopingCall(lambda: process_for_facebook.crawl(
            spider, keywords, exclusions, max_price, min_price, strictmode, facebook_city_id))
        task.start(60 * int(interval))
    else:
        task = LoopingCall(lambda: process.crawl(
            spider, keywords, exclusions, max_price, min_price, strictmode))
        task.start(60 * int(interval))


def create_config(config):
    config['DEFAULT'] = {
        'Keywords': "airpods,pro",
        'Exclusions': "case",
        'MaxPrice': "100",
        'MinPrice': "0",
        "EnableFacebook": "True",
        "EnableKijiji": "True",
        "EnableEbay": "True",
        "EnableAmazon": "True",
        "EnableLespacs": "True",
        "StrictMode": "True",
        "FacebookCityId": "110941395597405"
    }
    config.set(
        'DEFAULT', '; Facebook use the id of the closest city to you for the searches, if not set it will return no ads', None)
    config.set('DEFAULT', 'Interval', "10")
    config.set('DEFAULT', '; Every minutes the bot should scrape', None)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


main()
