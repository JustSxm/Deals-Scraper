import scrapy
import urllib.parse


class Amazon(scrapy.Spider):
    name = 'ebay'

    def __init__(self, keywords: list, exclusions: list,  max_price, min_price, strictmode, **kwargs):

        # build the URL
        self.exclusions = exclusions
        self.keywords = keywords
        self.strictmode = strictmode
        url = f"https://www.amazon.ca/s?k={'+'.join(keywords)}&rh=p_36%3A{int(min_price) * 100}-{int(max_price) * 100}"
        self.start_urls = [url]  # set the url to the spider
        super().__init__(**kwargs)

    def parse(self, response):
        # each flex item box (each ad)
        for ads in response.xpath('//div[@class="a-section a-spacing-base"]'):
            title = ads.xpath(
                './/span[@class="a-size-base-plus a-color-base a-text-normal"]/text()').extract_first()
            price = ads.xpath(
                './/span[@class="a-price-whole"]/text()').extract_first()

            # check for any exclusion is in the title, ignore if so
            if any(exclusions.lower() in title.lower() for exclusions in self.exclusions):
                continue
            # check if title has a keyword, in future this can be an option in the config (strictmode)
            if self.strictmode and not any(keywords.lower() in title.lower() for keywords in self.keywords):
                continue

            yield {
                'price': price,
                'title': title,
                'link': "https://www.amazon.ca" + ads.xpath('.//a/@href').extract_first(),
            }
