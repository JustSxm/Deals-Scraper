from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import re
from utils import click, set_interval, scroll, wait
import configparser


def main():
    config = configparser.ConfigParser(allow_no_value=True)
    if(len(config.read('config.ini')) < 1):
        config['DEFAULT'] = {
            'Keywords': "airpods,sealed",
            'Exclusions': "case",
            'MaxPrice': "100",
            'MinPrice': "0",
            "EnableFacebook": "false",
            'Where': "",
        }
        config.set('DEFAULT', '; keep where null for anywhere', None)
        config.set('DEFAULT', 'Interval', "5")
        config.set('DEFAULT', '; Every minutes the bot should scrape', None)
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
    config.read('config.ini')
    keywords = config['DEFAULT']['Keywords']
    keywords = keywords.split(",")
    exclusions = config['DEFAULT']['Exclusions']
    exclusions = exclusions.split(",")
    maxPrice = config['DEFAULT']['MaxPrice']
    minPrice = config['DEFAULT']['MinPrice']
    enableFacebook = config['DEFAULT']['EnableFacebook']
    where = config['DEFAULT']['Where']
    interval = config['DEFAULT']['Interval']
    if(enableFacebook):
        use_facebook(keywords, exclusions, maxPrice, minPrice, where)


def use_facebook(keywords: list, exclusions: list, maxPrice, minPrice, where):
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    driver.get("https://www.facebook.com/marketplace/")
    assert "Facebook" in driver.title
    searchbar = driver.find_element(
        By.CSS_SELECTOR, "[aria-label='Search Marketplace']")
    searchbar.clear()
    searchbar.send_keys(' '.join(keywords))
    searchbar.send_keys(Keys.RETURN)

    min = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Minimum Range']")))
    min.clear()
    min.send_keys(minPrice)

    max = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Maximum Range']")))
    max.clear()
    max.send_keys(maxPrice)
    max.send_keys(Keys.RETURN)

    sortby = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, "//*[text()='Sort by']")))
    click(driver, sortby)
    newestfirst = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, "//*[text()='Date listed: Newest first']")))
    click(driver, newestfirst)
    if(len(where) == 0):
        location = driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]')
        click(driver, location)
        radius = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Radius']")))
        click(driver, radius)
        km = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[text()='500 ']")))
        click(driver, km)
        apply = driver.find_element(
            By.XPATH, "//*[text()='Apply']")
        click(driver, apply)
    wait(5)
    scroll(driver)
    ads = driver.find_elements(By.CSS_SELECTOR,
                               "div.b3onmgus.ph5uu5jm.g5gj957u.buofh1pr.cbu4d94t.rj1gh0hx.j83agx80.rq0escxv.fnqts5cd.fo9g3nie.n1dktuyu.e5nlhep0.ecm0bbzt")
    hits = []
    for i in ads:
        try:
            price = i.find_element(By.CSS_SELECTOR,
                                   "span.d2edcug0.hpfvmrgz.qv66sw1b.c1et5uql.lr9zc1uh.a8c37x1j.fe6kdd0r.mau55g9w.c8b282yb.keod5gw0.nxhoafnm.aigsh9s9.d3f4x2em.mdeji52x.a5q79mjw.g1cxx5fr.lrazzd5p.oo9gr5id").text
            title = i.find_element(By.CSS_SELECTOR,
                                   "span.a8c37x1j.ni8dbmo4.stjgntxs.l9j0dhe7").text
            # check if title has exclusion keywords
            if any(exclusions.lower() in title.lower() for exclusions in exclusions):
                continue

            # check if title has a keyword, in future this can be an option in the config (strictmode)
            if not any(keywords.lower() in title.lower() for keywords in keywords):
                continue

            # get link
            link = i.find_element(By.CSS_SELECTOR, "a").get_attribute(
                "href").split("?")[0]
            hits.append(f'{title} - ${price}\n{link}\n\n\n')
        except:
            pass
        with open('hits.txt', 'wb') as f:
            f.write(''.join(hits).encode('utf-8'))
        # potentially send email?


main()
