import requests
#from selenium import webdriver
import time
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv

#Don't use selenium, not efficient enough
URL = "https://myanimelist.net/topanime.php"
#Change the link after running the script.
#second webpage is https://myanimelist.net/topanime.php?limit=50
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

                #browser = webdriver.Firefox()
                #browser.get(URL)
                #browseOff = False
#Allow the page to load and the script to run
time.sleep(5)
#Make a csv file that holds the data
#Current idea is to run the script 50 times and
#get the next anime in the table and
#add it to the csv file


                #browseOff = bool(input("------Close webpage?------\n"))
                #if browseOff:
                #    browser.close()
                #   browser.quit()
