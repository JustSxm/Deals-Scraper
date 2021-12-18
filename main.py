from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import configparser
# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()


def main():
    config = configparser.ConfigParser()
    if(len(config.read('config.ini')) < 1):
        config['DEFAULT'] = {
            'Keywords': ["airpods", "sealed"],
            'Exclusions': ["case"],
            'MaxPrice': "100",
            'MinPrice': "0",
            "EnableFacebook": "false",
        }
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
    config.read('config.ini')
    keywords = config['DEFAULT']['Keywords']
    exclusions = config['DEFAULT']['Exclusions']
    maxPrice = config['DEFAULT']['MaxPrice']
    minPrice = config['DEFAULT']['MinPrice']
    enableFacebook = config['DEFAULT']['EnableFacebook']

    print(keywords)
    print(exclusions)
    print(maxPrice)
    print(minPrice)
    print(enableFacebook)


main()
