import scrapy
import re


class Lespacs(scrapy.Spider):
    name = 'ebay'

    def __init__(self, keywords: list, exclusions: list,  max_price, min_price, strictmode, **kwargs):

        # build the URL
        self.exclusions = exclusions
        self.keywords = keywords
        self.strictmode = strictmode
        url = f"https://www.lespac.com/search/results.jsa?keywords={'+'.join(keywords)}&filterAction=true&textualSearchMode=normal&priceMin={min_price}&priceMax={max_price}&viewType=simplified&sortOrder=Date+desc"
        # lespacs uses geographical location to filter the results.
        url += "&geographicAreaIds=18578%2C13552%2C25561%2C21178%2C19376%2C16366%2C20173%2C22364%2C22961%2C22199%2C15770%2C23999%2C17373%2C19967%2C17569%2C26154%2C26188%2C26156%2C14990%2C14556&more_geographicAreaIds=18578&more_geographicAreaIds=13552&more_geographicAreaIds=25561&more_geographicAreaIds=21178&more_geographicAreaIds=19376&more_geographicAreaIds=16366&more_geographicAreaIds=20173&more_geographicAreaIds=22364&more_geographicAreaIds=22961&more_geographicAreaIds=22199&more_geographicAreaIds=15770&more_geographicAreaIds=23999&more_geographicAreaIds=17373&more_geographicAreaIds=19967&more_geographicAreaIds=17569&more_geographicAreaIds=26154&more_geographicAreaIds=26188&more_geographicAreaIds=26156&more_geographicAreaIds=14990&more_geographicAreaIds=14556"
        self.start_urls = [url]  # set the url to the spider
        super().__init__(**kwargs)

    def parse(self, response):
        # each flex item box (each ad)
        for ads in response.xpath('//div[@class="info"]'):
            title = ads.xpath(
                './a/text()').extract_first()
            price = ads.xpath(
                './span[@class="price"]/text()').extract_first()
            pattern = r'(\n)+(\t)+'
            # Remove new lines and random spaces from string
            title = re.sub(pattern, '', title)

            pattern = r' +'
            price = re.sub(pattern, '', price)
            # check for any exclusion is in the title, ignore if so
            if any(exclusions.lower() in title.lower() for exclusions in self.exclusions):
                continue

            # check if title has a keyword, in future this can be an option in the config (strictmode)
            if self.strictmode and not any(keywords.lower() in title.lower() for keywords in self.keywords):
                continue

            yield {
                'price': price,
                'title': title,
                'link': "https://www.lespac.com" + ads.xpath('./a/@href').extract_first(),
            }
