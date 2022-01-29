import scrapy
import urllib.parse
import re


class Kijiji(scrapy.Spider):
    name = 'kijiji'

    def __init__(self, keywords: list, exclusions: list,  max_price, min_price, strictmode, **kwargs):

        # build the URL
        self.exclusions = exclusions
        self.keywords = keywords
        self.strictmode = strictmode
        url = f"https://www.kijiji.ca/b-buy-sell/canada/{'-'.join(keywords)}/k0c10l0?"
        url += urllib.parse.urlencode(
            {'price': f"{min_price}__{max_price}", 'ad': 'offering'})
        self.start_urls = [url]  # set the url to the spider
        super().__init__(**kwargs)

    def parse(self, response):
        # each flex item box (each ad)
        for ads in response.xpath('//div[@data-listing-id]'):
            title = ads.xpath(
                './div/div[@class="info"]/div/div[@class="title"]/a/text()').extract_first()
            price = ads.xpath(
                './div/div[@class="info"]/div/div[@class="price"]/text()').extract_first()
            pattern = r'(\n)+ +'
            # Remove new lines and random spaces from string
            title = re.sub(pattern, '', title)
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
                'link': 'https://www.kijiji.ca' + ads.xpath('./div/div[@class="info"]/div/div[@class="title"]/a/@href').extract_first(),
            }
