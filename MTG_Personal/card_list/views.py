from django.shortcuts import render
from .models import Card
import schedule
import time
import threading
from selenium import webdriver                    
from selenium.webdriver.common.by import By  
from webdriver_manager.chrome import ChromeDriverManager


# Create your views here.
def index(request):
    cards = Card.objects.exclude(name__exact='')
    schedule.every().wednesday.at("13:00").do(scheduled_price_update,cards)
    stop_run_continuously = run_continuously()
    time.sleep(10)
    stop_run_continuously.set()
    return render(request, 'card_list/index.html', {'cards': cards})
    
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

def search_by_name(request):
    if request.method == "POST":
        query_name = request.POST.get('name')

        if query_name:
            results = Card.objects.filter(name__contains=query_name)
    return render(request,'card_list/card_search.html',{"results":results})


def scheduled_price_update(cards):
    print("Updating Prices")
    for each in cards:
        get_card_price(each)


def get_card_price(card):
    
    url = 'https://starcitygames.com/'

    browser_options = webdriver.ChromeOptions()
    browser_options.add_argument("--headless")
    # browser = webdriver.Chrome(ChromeDriverManager().install())
    browser = webdriver.Chrome(options=browser_options)
    browser.get(url)
    browser.implicitly_wait(20)
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
            foil_select=browser.find_element(By.XPATH, '//*[@id="hawkfacet_finish"]/li[1]/a')
            link = foil_select.get_attribute("href")
            print("It's Foil")
            browser.get(link)
        except:
            print("Element not interactable")
            return
    else:
        try:
            foil_select=browser.find_element(By.XPATH, '//*[@id="hawkfacet_finish"]/li[2]/a')
            link = foil_select.get_attribute("href")
            print("It's not foil")
            browser.get(link)
        except:
            print("Something went wrong")
            return            

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

