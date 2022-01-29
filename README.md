
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

# Deals Scraper

Deals Scraper is a Canadian tool to find good deals on websites like Facebook Marketplace, Kijiji, Ebay, Amazon and Lespacs


## Features

- Zooming fast
- Price Range (Min, Max)
- Keywords exclusion
- Strict mode (must have the keywords you mentionned)
- Repeating every amount of time specified
- Easily add your own website if you know what you're doing


## Installation


Clone the repo
```bash
  git clone https://github.com/JustSxm/Deals-Scraper.git
```

Install dependencies
```bash
  pip install -r requirement.txt
```

Edit the config file
```INI
[DEFAULT]
keywords = # the words you want to search for ex: airpods pro sealed
exclusions = # the words that will exclude ads ex: case
maxprice = # the max price of the item ex: 100
minprice = # the minimum price of the item ex: 10
enablefacebook = # if you want to enable facebook scraping ex: True
enablekijiji = # if you want to enable kijiji scraping ex: True
enableebay = # if you want to enable ebay scraping ex: True
enableamazon = # if you want to enable amazon scraping ex: True
enablelespacs = # if you want to enable lespacs scraping ex: True
strictmode = # if the title of the ads must contain atleast one keyword ex: True
facebookcityid = # https://www.facebook.com/places/Things-to-do-in-Toronto-Ontario/110941395597405/ ex: 110941395597405
; facebook use the id of the closest city to you for the searches, if not set it will return no ads
interval = 10
; every minutes the bot should scrape
```
    
## Running

Run the python script

```bash
  python main.py
```


## More information about each site

#### Facebook

Facebook uses a city to look around as it is not international, you can find the id by looking for your city on facebook and copy the id of their page.
(usually facebook.com/..../place/id)

Facebook is a good website for scraping.

#### Kijiji

Kijiji is a good website for scraping

#### Ebay

Ebay is an okay website for scraping

#### Amazon

Since Amazon is a vast website, it is way harder to find new ads and to precise what we want, therefore you will most likely get garbage from it than what you're actually looking.
It could be fine if you're looking for the cheapest price for a "popular" item

Amazon is a bad website for scraping

#### Lespacs

Lespacs is just like kijiji except it is more Quebec centered than Canada, therefore it can be a bad site for scraping if you are not from Quebec, otherwise it is a pretty good one

Outside of Quebec: Lespacs is a bad website for scraping
Inside of Quebec: Lespacs is a good website for scraping




## Acknowledgements

This project was made with the help of [scrapy](https://github.com/scrapy/scrapy)

## License

[MIT](https://choosealicense.com/licenses/mit/)

