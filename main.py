import configparser
from scrapy.crawler import CrawlerProcess
from websites.facebook import Facebook


def main():
    config = configparser.ConfigParser(allow_no_value=True)
    if(len(config.read('config.ini')) < 1):
        config['DEFAULT'] = {
            'Keywords': "airpods,sealed",
            'Exclusions': "case",
            'MaxPrice': "100",
            'MinPrice': "0",
            "EnableFacebook": "false",
            "FacebookCityId": "110941395597405"
        }
        config.set('DEFAULT', '; Facebook use the id of the closest city to you for the searches, if not set it will return no ads', None)
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
    facebook_city_id = config['DEFAULT']['FacebookCityId']
    interval = config['DEFAULT']['Interval']
    if(enable_facebook):
        process = CrawlerProcess(settings={"FEEDS": {"facebook.json": {"format": "json", "overwrite": True},}})
        process.crawl(Facebook, keywords, exclusions, max_price, min_price, facebook_city_id)
        process.start()

main()
