import configparser
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
            'Where': "",
        }
        config.set('DEFAULT', '; keep where null for anywhere', None)
        config.set('DEFAULT', 'Interval', "5")
        config.set('DEFAULT', '; Every minutes the bot should scrape', None)
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
    config.read('config.ini')
    keywords = config['DEFAULT']['Keywords']
    keywords = keywords.split(",")
    exclusions = config['DEFAULT']['Exclusions']
    exclusions = exclusions.split(",")
    maxPrice = config['DEFAULT']['MaxPrice']
    minPrice = config['DEFAULT']['MinPrice']
    enableFacebook = config['DEFAULT']['EnableFacebook']
    where = config['DEFAULT']['Where']
    interval = config['DEFAULT']['Interval']
    if(enableFacebook):
        Facebook(keywords, exclusions, maxPrice, minPrice, where)

main()
