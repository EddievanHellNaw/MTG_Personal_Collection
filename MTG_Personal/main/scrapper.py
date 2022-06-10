import schedule
import time
import threading
from selenium import webdriver                    
from selenium.webdriver.common.by import By  
import os


def schedule_price_update(cards):
    schedule.every().thursday.at("22:40").do(scheduled_price_update,cards)
    stop_run_continuously = run_continuously()
    time.sleep(3)
    stop_run_continuously.set()
    return cards

def run_continuously(interval=1):
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run


def scheduled_price_update(cards):
    print("Updating Prices")
    for each in cards:
        get_card_price(each)


def get_card_price(card):
    
    url = 'https://starcitygames.com/'

    browser_options = webdriver.ChromeOptions()
    browser_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    browser_options.add_argument("--headless")
    browser_options.add_argument("--disable-dev-shm-usage")
    browser_options.add_argument("--no-sandbox")
    browser = webdriver.Chrome(service=Service(executable_path=os.environ.get("CHROMEDRIVER_PATH")),
        options=browser_options)
    browser.get(url)
    browser.implicitly_wait(0.2)
    browser.maximize_window()

    print("Finding card...")
    print(card.name)
    if card.name is not None:
        try:
            browser.find_element(By.CSS_SELECTOR, "[name='search_query']").send_keys(str(card.name))
            search_button = browser.find_element(By.CLASS_NAME, "search-submit")
            search_button.click()
        except:
            print("Name's not valid")
            return

    if card.foil:
        print("Checking if Foil...")
        try:
            time.sleep(5)
            foil_select= browser.find_element(By.XPATH, '//*[@id="hawkfacet_finish"]/li[1]/a')
            link = foil_select.get_attribute("href")
            print("It's Foil")
            browser.get(link)
        except:
            print("Element not interactable")
            return
    else:
        try:
            time.sleep(5)
            foil_select=browser.find_element(By.XPATH, '//*[@id="hawkfacet_finish"]/li[2]/a')
            link = foil_select.get_attribute("href")
            print("It's not foil")
            browser.get(link)
        except:
            print("Something went wrong")
            return            
    time.sleep(5)
    cards = browser.find_elements(By.CLASS_NAME,"hawk-results-item")
    
    for each in cards:
        c = each.text
        price = each.find_element(By.XPATH, ".//descendant::div[contains(@class, 'price childAttributes')]")
        if card.expansion_name in c and card.price != price.text:
            card.price = price.text
        

    print(card.price)
    card.save()
    print("Price Updated")


    browser.quit()