import scrapy
from utils import print_info, print_scraper
from websites.facebook.models.Ad import Ad


class Facebook(scrapy.Spider):
    name = "facebook"

    def __init__(self, config, **kwargs):
        print_scraper("FACEBOOK", "Starting...")
        city_id = config["FACEBOOK"]["CityId"]
        min_price = config["FACEBOOK"]["MinPrice"]
        max_price = config["FACEBOOK"]["MaxPrice"]
        sort_by = config["FACEBOOK"]["SortBy"]
        keywords = '%20'.join(config["DEFAULT"]["Keywords"].split(" "))
        self.keywords = config["DEFAULT"]["Keywords"].split(" ")
        self.exclusions = config["DEFAULT"]["Exclusions"].split(" ")
        self.strictmode = config["DEFAULT"].getboolean("StrictMode")
        self.start_urls = ["https://www.facebook.com/marketplace/" + city_id + "/search?minPrice=" + min_price +
                           "&maxPrice=" + max_price + "&daysSinceListed=1" + "&sortBy=" + sort_by + "&query=" + keywords]
        print_scraper("FACEBOOK", "Started !")
        super().__init__(**kwargs)

    def parse(self, response):
        print_scraper("FACEBOOK", "Scraping...")
        allAds = []
        not_found_selector = response.css("div span::text").getall()

        # Skip if no ads found around 60 km
        if "No results found for " in not_found_selector:
            print_scraper("FACEBOOK", "No results found")
            return None
        print_scraper("FACEBOOK", "Found ads")
        # each flex item box (each ad)
        flex_selector = response.css(
            "div.x8gbvx8.x78zum5.x1q0g3np.x1a02dak.x1nhvcw1.x1rdy4ex.xcud41i.x4vbgl9.x139jcc6 > div")
        for ads in flex_selector:
            try:
                title = ads.css('span::text').getall()[1];

                # Skip if title contains any of the exclusion keywords
                if any(exclusions.lower() in title.lower() for exclusions in self.exclusions):
                    continue

                # Skip if title does not contain any of the keywords (if strict mode is enabled)
                if self.strictmode and not any(x.lower() in title.lower() for x in self.keywords) :
                    continue
                    
                ad = Ad()
                ad["title"] = title
                ad["price"] = ads.css('span::text').extract_first()
                ad["link"] = 'https://www.facebook.com' + ads.css('a::attr(href)').extract_first()
                print_scraper("FACEBOOK", "An ad fitting the criterias was found")
                allAds.append(ad)
            except:
                pass
        return allAds
