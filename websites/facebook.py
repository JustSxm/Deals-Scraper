import scrapy
import urllib.parse
from utils import click, set_interval, scroll, wait


class Facebook(scrapy.Spider):
    name = 'facebook'
    # move to scrapy and append parameters with urllib instead of using selenium
    def __init__(self, keywords: list, maxPrice, minPrice, **kwargs):
        #
        url = "https://www.facebook.com/marketplace/search?"
        url += urllib.parse.urlencode({'query': ' '.join(keywords), 'minPrice': minPrice, 'maxPrice': maxPrice, 'sortBy': 'creation_time_descend'})
        self.start_urls = [url]
        super().__init__(**kwargs)

    def parse(self, response):
        for ads in response.css('div.b3onmgus.ph5uu5jm.g5gj957u.buofh1pr.cbu4d94t.rj1gh0hx.j83agx80.rq0escxv.fnqts5cd.fo9g3nie.n1dktuyu.e5nlhep0.ecm0bbzt'):
            yield {
                'price': ads.css("span.d2edcug0.hpfvmrgz.qv66sw1b.c1et5uql.lr9zc1uh.a8c37x1j.fe6kdd0r.mau55g9w.c8b282yb.keod5gw0.nxhoafnm.aigsh9s9.d3f4x2em.mdeji52x.a5q79mjw.g1cxx5fr.lrazzd5p.oo9gr5id/text()").extract_first(),
                'title': ads.css('span.a8c37x1j.ni8dbmo4.stjgntxs.l9j0dhe7/text()').extract_first(),
                'link': ads.css('a::attr(href)').extract_first(),
            }

"""
    if any(exclusions.lower() in title.lower() for exclusions in exclusions):
        continue

    # check if title has a keyword, in future this can be an option in the config (strictmode)
    if not any(keywords.lower() in title.lower() for keywords in keywords):
        continue
"""

