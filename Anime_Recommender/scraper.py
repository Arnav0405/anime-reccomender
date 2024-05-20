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
#print(soup.find_all('tr'))

#Get the table that holds the anime
lists = []
temp_lst = []

#Get a table header list inside the list, as the first list.
#maybe using Pandas would be better, but idrk how I would implement it....
table_header = soup.find('tr', attrs={'class':'table-header'})
for row in table_header.find_all('td'):
    temp_lst.append(row.text)
lists.append(temp_lst)

#Now let's get the tr with class in ranking-list
top_Fifty = soup.find_all('tr', attrs={'class':'ranking-list'})
for row in top_Fifty:
    anime = {}     
    for col in row:
        print(col)
        #anime[lists[0][0]] = col.
        #anime[lists[0][1]] = col.
    lists.append(anime)
#print(lists)


#Make a csv file that holds the data
#Current idea is to run the script 50 times and
#get the next anime in the table and
#add it to the csv file