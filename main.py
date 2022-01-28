import configparser
from scrapy.crawler import CrawlerProcess
from websites.facebook import Facebook
from websites.kijiji import Kijiji


def main():
    config = configparser.ConfigParser(allow_no_value=True)
    if(len(config.read('config.ini')) < 1):
        config['DEFAULT'] = {
            'Keywords': "airpods,sealed",
            'Exclusions': "case",
            'MaxPrice': "100",
            'MinPrice': "0",
            "EnableFacebook": "false",
            "EnableKijiji": "false",
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
    facebook_city_id = config['DEFAULT']['FacebookCityId']
    interval = config['DEFAULT']['Interval']
    enable_facebook = False  # TODO: Remove once done
    if(enable_facebook):
        process = CrawlerProcess(
            settings={"FEEDS": {"facebook.json": {"format": "json", "overwrite": True}, }, "USER_AGENT": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36)'})
        process.crawl(Facebook, keywords, exclusions,
                      max_price, min_price, facebook_city_id)
        process.start()
    if(enable_kijiji):
        process = CrawlerProcess(
            settings={"FEEDS": {"kijiji.json": {"format": "json", "overwrite": True}, }, "USER_AGENT": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36)'})  # Kijiji has anti scraping method using the user agent
        process.crawl(Kijiji, keywords, exclusions,
                      max_price, min_price)
        process.start()


main()
