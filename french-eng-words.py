import requests
from bs4 import BeautifulSoup as Craft

def fetch():
    url = ""
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
            Data_ = tbody.findAll("td")
            Index = Heads[0].text.strip()
            French = Heads[1].text strip()
            English = Heads[2].text.strip()
            words.write("{0} \t {1} \t {2}".format(Index,French, English))
        words.close()
