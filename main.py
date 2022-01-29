import configparser
from scrapy.crawler import CrawlerProcess
from websites.amazon import Amazon
from websites.ebay import Ebay
from websites.facebook import Facebook
from websites.kijiji import Kijiji
from websites.lespacs import Lespacs


def main():
    config = configparser.ConfigParser(allow_no_value=True)
    if(len(config.read('config.ini')) < 1):
        config['DEFAULT'] = {
            'Keywords': "airpods,pro",
            'Exclusions': "case",
            'MaxPrice': "100",
            'MinPrice': "0",
            "EnableFacebook": "false",
            "EnableKijiji": "false",
            "EnableEbay": "false",
            "EnableAmazon": "false",
            "EnableLespacs": "false",
            "FacebookCityId": "110941395597405"
        }
        config.set(
            'DEFAULT', '; Facebook use the id of the closest city to you for the searches, if not set it will return no ads', None)
        config.set('DEFAULT', 'Interval', "5")
        config.set('DEFAULT', '; Every minutes the bot should scrape', None)
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
    config.read('config.ini')
    keywords = config['DEFAULT']['Keywords']
    keywords = keywords.split(",")
    exclusions = config['DEFAULT']['Exclusions']
    exclusions = exclusions.split(",")
    max_price = config['DEFAULT']['MaxPrice']
    min_price = config['DEFAULT']['MinPrice']
    enable_facebook = config['DEFAULT']['EnableFacebook']
    enable_kijiji = config['DEFAULT']['EnableKijiji']
    enable_ebay = config['DEFAULT']['EnableEbay']
    enable_amazon = config['DEFAULT']['EnableAmazon']
    enable_lespacs = config['DEFAULT']['EnableLespacs']
    facebook_city_id = config['DEFAULT']['FacebookCityId']
    interval = config['DEFAULT']['Interval']
    enable_facebook = False  # TODO: Remove once done
    enable_kijiji = False  # TODO: Remove once done
    enable_ebay = False  # TODO: Remove once done
    enable_amazon = False  # TODO: Remove once done
    if(enable_facebook):
        scrape(Facebook, "facebook.json", keywords,
               exclusions, max_price, min_price, facebook_city_id)
    if(enable_kijiji):
        scrape(Kijiji, "kijiji.json", keywords,
               exclusions, max_price, min_price)
    if(enable_ebay):
        scrape(Ebay, "ebay.json", keywords, exclusions, max_price, min_price)
    if(enable_amazon):
        scrape(Amazon, "amazon.json", keywords,
               exclusions, max_price, min_price)
    if(enable_lespacs):
        scrape(Lespacs, "lespacs.json", keywords,
               exclusions, max_price, min_price)


def scrape(spider, json, keywords: list, exclusions: list, max_price, min_price, facebook_city_id=None):
    process = CrawlerProcess(
        settings={"FEEDS": {json: {"format": "json", "overwrite": True}, }, "USER_AGENT": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36)'})  # Kijiji has anti scraping method using the user agent
    if(facebook_city_id):
        process.crawl(spider, keywords, exclusions,
                      max_price, min_price, facebook_city_id)
    else:
        process.crawl(spider, keywords, exclusions, max_price, min_price)
    process.start()


main()
