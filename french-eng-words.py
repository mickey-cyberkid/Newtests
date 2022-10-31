import requests
from bs4 import BeautifulSoup as Craft

def fetch():
    url = "https://strommeninc.com/1000-most-common-french-words-frequency-vocabulary/"
    Page = requests.get(url)
    page_content = Page.content
    scrap(page_content)

def scrap(page_content):
    Crafted = Craft(page_content,'html.parser')
    Table_div = Crafted.find("div", class_="entry-content clear")
    Table = Table_div.find("table")
    Tbody = Table.find("tbody")
    Data_set = Tbody.findAll("tr")
    with open("wordlist.txt",'a') as words:
        for row in Data_set:
            Data_ = row.findAll("td")
            Index = Data_[0].text.strip()
            French = Data_[1].text.strip()
            English = Data_[2].text.strip()
            words.write("{0} \t {1} \t {2}".format(Index,French, English))
        words.close()

fetch()
