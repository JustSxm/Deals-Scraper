from scrapy import Field, Item


class Ad(Item):
    title = Field()
    price = Field()
    link = Field()
