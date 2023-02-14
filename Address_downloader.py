

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

import time
import timeit
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


monday='https://goo.gl/maps/ucVt17nYzVyyMRDx6'
tuesday='https://goo.gl/maps/Hr46uKGEGRWwdunQ7'
wednesday='https://goo.gl/maps/VEPfwsMvigioE4fn7'
thursday='https://goo.gl/maps/o5D5XZ1XgcEG5LNJ7'
friday='https://goo.gl/maps/sGkKt7TmGqBxwMmJA'





driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(monday)
start = timeit.default_timer()

# identify scrolling element first i.e. the sidebar
scrolling_element_xpath = '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[5]'
scrolling_element= driver.find_element(By.XPATH, scrolling_element_xpath)

# use height of element to determine if need to scroll 
last_height = driver.execute_script("return arguments[0].scrollHeight", scrolling_element)
print(last_height)

SCROLL_PAUSE_TIME = 2.0 # pause before next scroll, to let page load 
t = 0 # number of times we have scrolled

## Loop the scrolling until cannot scroll anymore
while True:
    print(t)
    # Scroll down to bottom of whatever is currently loaded
    driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight)', scrolling_element)
    t = t+1

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Check if more scrolling required 
    new_height = driver.execute_script("return arguments[0].scrollHeight", scrolling_element)
    print(new_height)
    if new_height == last_height:
        break
    last_height = new_height


stop = timeit.default_timer()

print('Time taken: ', stop - start) 




address = driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[5]')
address.text




split_list=address.text.split("\n")
split_list




#Group into two elements
grouped_list = []
for i in range(0, len(split_list), 2):
    grouped_list.append((split_list[i],split_list[i+1]))

#Get rid of parentheses and commas from each element
grouped_string_list = []
for pair in grouped_list:
    grouped_string_list.append(", ".join(pair))
grouped_string_list
len(grouped_string_list)



monday_list=grouped_string_list

