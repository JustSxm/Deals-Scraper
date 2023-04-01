import urllib.parse

import scrapy

from Ad import Ad
from utils import print_info, print_scraper


class Ebay(scrapy.Spider):
    name = 'ebay'

    def __init__(self, config, **kwargs):
        print_scraper("EBAY", "Starting...")
        # build the URL
        self.keywords = config["DEFAULT"]["Keywords"].split(" ")
        self.exclusions = config["DEFAULT"]["Exclusions"].split(" ")
        self.strictmode = config["DEFAULT"].getboolean("StrictMode")
        min_price = config["EBAY"]["MinPrice"]
        max_price = config["EBAY"]["MaxPrice"]
        url = f"https://www.ebay.com/sch/i.html?"
        url += urllib.parse.urlencode(  # LH_BIN = buy it now, _sop = newly listed
            {'_nkw': ' '.join(self.keywords), '_sop': '10', 'LH_BIN': '1', '_udlo': min_price, '_udhi': max_price})
        self.start_urls = [url]  # set the url to the spider
        super().__init__(**kwargs)

    def parse(self, response):
        print_scraper("EBAY", "Scraping...")
        allAds = []

        if(response.xpath('//*[@id="srp-river-results"]/ul/li') == None):
            print_scraper("EBAY", "No results found")
            return None
        print_scraper("EBAY", "Ads found")

        # each flex item box (each ad)
        for ads in response.xpath('//li[@class="s-item s-item__pl-on-bottom"]'):
            title = ads.xpath(
                './/div[@class="s-item__title"]/span/text()').extract_first()
            price = ads.xpath(
                './/span[@class="s-item__price"]/text()').extract_first()
            # ebay has "1$ to 2$" options and those are definetly not what we are looking for.
            if price == None:
                continue

            # ebay has ads who are usually unrelated to our specific search.
            if title == None or title == "Shop on eBay":
                continue
            # check for any exclusion is in the title, ignore if so
            if any(exclusions.lower() in title.lower() for exclusions in self.exclusions):
                continue

            # check if title has a keyword, in future this can be an option in the config (strictmode)
            if self.strictmode and not any(keywords.lower() in title.lower() for keywords in self.keywords):
                continue

            ad = Ad()
            ad["title"] = title
            ad["price"] = price
            ad["link"] = ads.xpath('.//a[@class="s-item__link"]/@href').extract_first()
            print_scraper("EBAY", "An ad fitting the criterias was found")
            allAds.append(ad)
        return allAds