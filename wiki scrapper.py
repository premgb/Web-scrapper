#############################################################################
# scrap webpage to get a wikitable of highest grossing films from Wikipedia #
#############################################################################
#
import requests
from bs4 import BeautifulSoup
import pandas as pd
 
'''
http_proxy  = "http:<your proxy> "
https_proxy = "http:<your proxy> "
 
proxyDict = {
              "http"  : http_proxy,
              "https" : https_proxy,
            }
 
page = requests.get("https://en.wikipedia.org/wiki/List_of_highest-grossing_films#Highest-grossing_films", proxies=proxyDict)
'''
page = requests.get("https://en.wikipedia.org/wiki/List_of_highest-grossing_films#Highest-grossing_films")
soup = BeautifulSoup(page.content, "html.parser")
table = soup.find_all('table', class_='wikitable sortable plainrowheaders')[0]
#print(table[0].prettify())
 
columns_header = [th.getText() for th in
                  table.findAll('tr')[0].findAll('th')]
 
data_rows=table.findAll('tr')[1:]
data=[[td.getText() for td in data_rows[i].findAll(['td', 'th'])]
            for i in range(len(data_rows))]
 
df=pd.DataFrame(data, columns=columns_header)
print df.head()
