import requests
from bs4 import BeautifulSoup
import csv

#Don't use selenium, not efficient enough
URL = "https://myanimelist.net/topanime.php"
#Change the link after running the script.
#second webpage is https://myanimelist.net/topanime.php?limit=50
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
#print(soup.prettify())
print(soup.find_all('tr'))
#Get the table that holds the anime
header = []

table = soup.find('table', attrs = {'class':'table-header'})
#print(soup.table.prettify())
#Make a csv file that holds the data
#Current idea is to run the script 50 times and
#get the next anime in the table and
#add it to the csv file


                #browseOff = bool(input("------Close webpage?------\n"))
                #if browseOff:
                #    browser.close()
                #   browser.quit()
