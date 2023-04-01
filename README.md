
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

#### Please star the repo if you found it useful! Thank you!

# Deals Scraper

<details>
<summary>Table of Contents</summary>
 
- [Features](#features)  
- [Requirement](#Requirement)  
- [Configuration](#Configuration)  
  - [Facebook](#FacebookConfiguration)  
  - [Kijiji](#KijijiConfiguration)  
  - [Ebay](#EbayConfiguration)  
  - [Lespacs](#LespacsConfiguration)  
  - [Amazon](#AmazonConfiguration)  
- [Running](#Running)  
- [More information about each site](#Moreinformationabouteachsite)  
  - [Facebook](#Facebook)  
  - [Kijiji](#Kijiji)  
  - [Ebay](#Ebay)  
  - [Lespacs](#Lespacs)  
  - [Amazon](#Amazon)  
- [Acknowledgements](#Acknowledgements)  
- [Contributors](#Contributors)  
- [License](#License)
 
</details>

Deals Scraper is a Canadian tool to find good deals on websites like Facebook Marketplace, Kijiji, Ebay, Amazon and Lespacs


<a name="features"/>

## Features

- Zooming fast
- Specify a price range (Min & Max) per scraper
- Blacklist keywords from the scraping
- Strict mode so only ads containing your keywords are picked
- Schedule the project to run on a recurring basis
- Easily add your own website if you know what you're doing

<a name="Requirement"/>

## Requirement

 - [Python](https://www.python.org/)
<a name="Installation"/>

## Installation


Clone the repo
```bash
  git clone https://github.com/JustSxm/Deals-Scraper.git
```

Install dependencies
```bash
  pip install -r requirement.txt
```
<a name="Configuration"/>

## Configuration
<a name="DefaultConfiguration"/>

## Default Configuration
Open the config file (config.ini) and find the section named DEFAULT
```INI
[DEFAULT]
Keywords = airpods pro
Exclusions = case
StrictMode = False
Interval = 1
```
- Keywords: This config sets the keywords that the software will search for.
- Exclusions: This config sets the words or phrases that the software will ignore.
- StrictMode: This config determines whether the software will strictly match the keywords and exclusions or be more flexible in its search.
- Interval: This config sets the time interval for how often the software will search for the keywords in minutes.
<a name="FacebookConfiguration"/>

### Facebook
Open the config file (config.ini) and find the section named FACEBOOK
```INI
[FACEBOOK]
Enabled = True
CityId = 
MinPrice = 0
MaxPrice = 1000
SortBy = distance_ascend
; best_match, price_ascend, price_descend, distance_ascend, creation_time_descend
```
- Enabled: This config determines whether the Facebook module is enabled (True) or disabled (False).
- CityId: This config sets the ID for the desired city or location for the Facebook search.
- MinPrice: This config sets the minimum price range for the Facebook search.
- MaxPrice: This config sets the maximum price range for the Facebook search.
- SortBy: This config sets the sorting method for the Facebook search results. Available options include "best_match" (sorted by Facebook's relevance algorithm), "price_ascend" (sorted by price in ascending order), "price_descend" (sorted by price in descending order), "distance_ascend" (sorted by distance in ascending order), and "creation_time_descend" (sorted by time in descending order).

To find your CityId:
- go to facebook and search for your city (Ex: https://www.facebook.com/search/top?q=toronto)
- Click on "Places" <br>
![Image of Place button](https://i.imgur.com/6uquG7S.png)
- Click on your city <br>
![Image of Toronto City](https://i.imgur.com/6ipzFG5.png)
- Copy your city's id <br>
![Image of Toronto City's URL](https://i.imgur.com/sCmi2jW.png)

After make sure to login to Facebook, this scraper uses your browser to scrape, it doesn't connect automatically.
<a name="KijijiConfiguration"/>

## Kijiji
Open the config file (config.ini) and find the section named Kijiji
```INI
[KIJIJI]
Enabled = True
CityUrl = 
Identifier = 
MinPrice = 20
MaxPrice = 100
Type = ownr
; ownr, delr, all
```
- Enabled: This config determines whether the Kijiji module is enabled (True) or disabled (False).
- CityUrl: This config sets the URL for the Kijiji website for the desired city or location.
- Identifier: The identifier with the city url.
- MinPrice: This config sets the minimum price range for the Kijiji search.
- MaxPrice: This config sets the maximum price range for the Kijiji search.
- Type: This config sets the type of Kijiji ads to search for, which can be "ownr" (owner-sold ads), "delr" (dealer-sold ads), or "all" (both types).

To find your CityId and Identifier:
- go to kijiji and search for something random with ads results
- Copy your city's id and identifier <br>
![Image of Kijiji City's URL](https://i.imgur.com/6e3UUnv.png)
<a name="EbayConfiguration"/>

## Ebay
Open the config file (config.ini) and find the section named Ebay
```INI
[EBAY]
Enabled = True
MinPrice = 20
MaxPrice = 100
```
- Enabled: This config determines whether the eBay module is enabled (True) or disabled (False).
- MinPrice: This config sets the minimum price range for the eBay search.
- MaxPrice: This config sets the maximum price range for the eBay search.
<a name="LespacsConfiguration"/>

## Lespacs
The LesPACs configuration provided in this repository is not currently implemented due to the website either undergoing a rewrite or implementing security measures to prevent web scraping.
Unfortunately, without more information from LesPACs themselves, it is not possible to provide an ETA for when the configuration will be functional again.
<a name="AmazonConfiguration"/>

## Amazon
If you are looking to use the Amazon configuration in this repository, please note that it is not included in the current version and is not planned to be included in the future. This is due to the implementation of anti-scraping measures on the Amazon website, such as CAPTCHAs, which make it difficult or impossible to retrieve data using a web scraper. As such, the Amazon configuration provided in previous versions of the repository may no longer be functional.
<a name="Running"/>

## Running

Run the python script

```bash
  python main.py
```

<a name="Moreinformationabouteachsite"/>

## More information about each site
<a name="Facebook"/>

#### Facebook

Facebook uses a city to look around as it is not international, you can find the id by looking for your city on facebook and copy the id of their page.
(usually facebook.com/..../place/id)

Facebook is a good website for scraping.
<a name="Kijiji"/>

#### Kijiji

Kijiji is a good website for scraping
<a name="Ebay"/>
#### Ebay

Ebay is an okay website for scraping
<a name="Amazon"/>

#### Amazon

Since Amazon is a vast website, it is way harder to find new ads and to precise what we want, therefore you will most likely get garbage from it than what you're actually looking.
It could be fine if you're looking for the cheapest price for a "popular" item

Amazon is a bad website for scraping
<a name="Lespacs"/>

#### Lespacs

Lespacs is just like kijiji except it is more Quebec centered than Canada, therefore it can be a bad site for scraping if you are not from Quebec, otherwise it is a pretty good one

Outside of Quebec: Lespacs is a bad website for scraping

Inside of Quebec: Lespacs is a good website for scraping



<a name="Acknowledgements"/>

## Acknowledgements

This project was made with the help of [scrapy](https://github.com/scrapy/scrapy)
<a name="Contributors"/>
## Contributors
README - [ChatGPT](https://chat.openai.com/chat)
<a name="License"/>
## License

[MIT](https://choosealicense.com/licenses/mit/)

