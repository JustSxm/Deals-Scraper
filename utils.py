from selenium.webdriver.common.action_chains import ActionChains
import threading
import time


# Click on an element like a human because facebook uses divs instead of buttons
def click(driver, element):
    ActionChains(driver).move_to_element(element).click().perform()


# Run a function periodically
def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


# scroll to the bottom of the page 5 times to load more results
def scroll(driver):
    SCROLL_PAUSE_TIME = 0.5
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    for i in range(5):
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
