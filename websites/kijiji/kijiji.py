import scrapy
from utils import print_info, print_scraper
from websites.kijiji.models.Ad import Ad


class Kijiji(scrapy.Spider):
    name = "kijiji"

    def __init__(self, config, **kwargs):
        print_scraper("KIJIJI", "Starting...")
        city_url = config["KIJIJI"]["CityUrl"]
        min_price = config["KIJIJI"]["MinPrice"]
        max_price = config["KIJIJI"]["MaxPrice"]
        identifier = config["KIJIJI"]["Identifier"]
        keywords = '-'.join(config["DEFAULT"]["Keywords"].split(" "))
        type = config["KIJIJI"]["Type"]
        self.keywords = config["DEFAULT"]["Keywords"].split(" ")
        self.exclusions = config["DEFAULT"]["Exclusions"].split(" ")
        self.strictmode = config["DEFAULT"].getboolean("StrictMode")
        
        if type == "all":
            self.start_urls = ["https://www.kijiji.ca/" + city_url + "/" + keywords + "/" + identifier +  f"?{min_price}__{max_price}"]
        else:
            self.start_urls = ["https://www.kijiji.ca/" + city_url + "/" + keywords + "/" + identifier +  f"?{min_price}__{max_price}?&a-vendre-par={type}"]
        print_scraper("KIJIJI", "Started !")
        super().__init__(**kwargs)

    def parse(self, response):
        print_scraper("KIJIJI", "Scraping...")
        allAds = []
        not_found_selector = response.css("h4.zero-results")

        # Skip if no ads found around 60 km
        if len(not_found_selector) > 0:
            print_scraper("KIJIJI", "No results found")
            return None
        print_scraper("KIJIJI", "Found ads")
        # each flex item box (each ad)
        flex_selector = response.css(".regular-ad")
        for ads in flex_selector:
            try:
                title = ads.css('div.title a::text').get().strip()

                # Skip if title contains any of the exclusion keywords
                if any(exclusions.lower() in title.lower() for exclusions in self.exclusions):
                    continue

                # Skip if title does not contain any of the keywords (if strict mode is enabled)
                if self.strictmode and not any(x.lower() in title.lower() for x in self.keywords) :
                    continue
                    
                ad = Ad()
                ad["title"] = title
                ad["price"] = ads.css("div.price::text").get().strip()
                ad["link"] = 'https://www.kijiji.ca' + ads.css('a::attr(href)').extract_first()
                print_scraper("KIJIJI", "An ad fitting the criterias was found")
                allAds.append(ad)
            except:
                pass
        return allAds
