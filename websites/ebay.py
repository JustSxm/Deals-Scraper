import scrapy
import urllib.parse


class Ebay(scrapy.Spider):
    name = 'ebay'

    def __init__(self, keywords: list, exclusions: list,  max_price, min_price, strictmode, **kwargs):

        # build the URL
        self.exclusions = exclusions
        self.keywords = keywords
        self.strictmode = strictmode
        url = f"https://www.ebay.com/sch/i.html?"
        url += urllib.parse.urlencode(  # LH_BIN = buy it now, _sop = newly listed
            {'_nkw': ' '.join(keywords), '_sop': '10', 'LH_BIN': '1', '_udlo': min_price, '_udhi': max_price})
        self.start_urls = [url]  # set the url to the spider
        super().__init__(**kwargs)

    def parse(self, response):
        # each flex item box (each ad)
        for ads in response.xpath('//*[@id="srp-river-results"]/ul/li'):
            title = ads.xpath(
                './/h3[@class="s-item__title"]/text()').extract_first()
            price = ads.xpath(
                './/span[@class="s-item__price"]/text()').extract_first()
            # ebay has "1$ to 2$" options and those are definetly not what we are looking for.
            if price == None:
                continue

            # ebay has ads who are usually unrelated to our specific search.
            if title == None:
                continue
            # check for any exclusion is in the title, ignore if so
            if any(exclusions.lower() in title.lower() for exclusions in self.exclusions):
                continue

            # check if title has a keyword, in future this can be an option in the config (strictmode)
            if self.strictmode and not any(keywords.lower() in title.lower() for keywords in self.keywords):
                continue

            yield {
                'price': price,
                'title': title,
                'link': ads.xpath('.//a[@class="s-item__link"]/@href').extract_first(),
            }
