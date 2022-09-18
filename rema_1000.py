from selenium import webdriver
import time
import sys
import os

class grocery_item:
    def __init__(self, name, info, price):
        self.name = name
        self.info = info
        self.price = price
    
url = 'https://rema1000.dk/avis'
driver = webdriver.Chrome("/Users/maxvisser/Documents/Code/selenium_installation/chromedriver")

driver.get('https://rema1000.dk/avis') # fetch website

#if they ask for cookies, decline them
try:
    driver.find_element_by_xpath('//*[@id="declineButton"]').click()
    time.sleep(2)
except:
    print("did not ask for cookies preferences")
finally:
    
    # find current tilbudsavis
    # TODO make general, so when it updates, it selects the most current one
    driver.find_element_by_xpath('//*[@id="list-publications"]/div[1]/ul/li[1]').click()
    
    time.sleep(0.5) 
    
    driver.find_element_by_xpath('//*[@id="sgn-publication-viewer-container"]/div/div[1]/div/div/div/div[1]/button[3]').click()
    
    time.sleep(0.5)
    
    driver.find_element_by_xpath('//*[@id="sgn-publication-viewer-container"]/div/div[3]/div[2]/div/div[4]/button[2]').click()
    
    responds = driver.find_element_by_xpath('//*[@id="sgn-publication-viewer-container"]/div/div[3]/div[2]/div/div[5]/div[2]/div/div/div/ol')
    
    offers = responds.find_elements_by_class_name(name="sgn-offers-list-item-container")
    
    items = []
for item in offers:
    item.find_element_by_class_name("sgn-offers-content-container")
    item.find_element_by_class_name("sgn-offers-content-text")
    item.find_element_by_class_name("sgn-offers-content-heading")
    item.find_element_by_tag_name('span')
    
    info = item.text.split("\n") # list of descriptions for item
    
    
    item_name = info[0]
    item_price = float(info[-1].strip().strip(" .kr").replace(",", "."))

    if len(info[1]) > 8:
        item_info = info[1]
        items.append(grocery_item(item_name, item_info, item_price))
    else:
        items.append(grocery_item(item_name, "no info", item_price))
    
    return_string = ''
    for item in items:
        print("Found these offers:")
        print(f"{item.name} koster {item.price}")
        print(item.info)
        return_string += f"{item.name} costs {item.price} kr\n"
        
    with open("offers.txt", "w") as f:
            f.write(return_string)
            
    
driver.quit() # quit the driver