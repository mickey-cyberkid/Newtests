#-*- coding:utf-8 -*-
import os
import sys
import ssl
import time
import mechanize
from urllib.request import urlopen as Goto
from bs4 import BeautifulSoup as Craft


ssl._create_default_https_context = ssl._create_unverified_context
browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.set_handle_refresh(True)
browser.set_handle_equiv(True)
browser.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; de) Opera 8.0')]


def anim(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.008)


def scrap(page_content):
    Crafted = Craft(page_content,"html.parser")
    holder = Crafted.find('div',class_="topgamedetails")
    body = holder.findAll("div",class_="fulltipdivs")
    total_odds = holder.find('span',class_="totlasdivs directleft").text.strip()
    for match in body:
        league = match.find("span",{"class":"checkleaguecss"})
        league = league.text.strip()
        teams = match.find("a",{"class":"gamelink"})
        teams =teams.text.strip().split(" v ")
        home = teams[0]
        away = teams[1]
        prediction = match.find("span",class_="checktipcss")
        prediction = prediction.text.strip()
        print("\033[1;36m[💸]League : {}".format(league))
        print("\033[1;33m[⚽️]{0}   \tVs\t {1}".format(home,away))
        print("\033[1;32m[🔵]Prediction : {}".format(str(prediction)))

    print("\033[1;32m {}".format(total_odds))


def check(tip):
    if "1" in tip:
       return "HOME"
    elif "2" in tip:
       return "AWAY"
    elif "X" in tip:
       return "DRAW"
    else:
       pass


def banner():
    ban = '''
\t @@@@@@    @@@@@@       @@@@@@   @@@  @@@  @@@@@@@   @@@@@@@@  
\t@@@@@@@@  @@@@@@@@     @@@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@@  
\t@@!  @@@  @@!  @@@     !@@       @@!  @@@  @@!  @@@  @@!       
\t!@!  @!@  !@!  @!@     !@!       !@!  @!@  !@!  @!@  !@!       
\t!!@!!@!!   !@!!@! per  !!@@!!    @!@  !@!  @!@!!@!   @!!!:!    
\t  !!@!!!   !!@!!! cent  !!@!!!   !@!  !!!  !!@!@!    !!!!!:    
\t     !!!  !!:  !!!          !:!  !!:  !!!  !!: :!!   !!:       
\t     !:!  :!:  !:!         !:!   :!:  !:!  :!:  !:!  :!:       
\t::::: ::  ::::: ::     :::: ::   ::::: ::  ::   :::   :: ::::  
\t : :  :    : :  :      :: : :     : :  :    :   : :  : :: ::   
\t                             
\t\t@@@@@@@   @@@@@@@@  @@@@@@@  
\t\t@@@@@@@@  @@@@@@@@  @@@@@@@  
\t\t@@!  @@@  @@!         @@!    
\t\t!@   @!@  !@!         !@!    
\t\t@!@!@!@   @!!!:!      @!!    
\t\t!!!@!!!!  !!!!!:      !!!    
\t\t!!:  !!!  !!:         !!:    
\t\t:!:  !:!  :!:         :!:    
\t\t :: ::::   :: ::::     :: By: MCyberkid
\t\t:: : ::   : :: ::      :

'''
    ban2 = '''
  ______    ______         __    __         ______   __    __  _______   ________ 
 /      \  /      \       /  |  /  |       /      \ /  |  /  |/       \ /        |
/$$$$$$  |/$$$$$$  |      $$/  /$$/       /$$$$$$  |$$ |  $$ |$$$$$$$  |$$$$$$$$/ 
$$ \__$$ |$$ \__$$ |          /$$/        $$ \__$$/ $$ |  $$ |$$ |__$$ |$$ |__    
$$    $$ |$$    $$<          /$$/         $$      \ $$ |  $$ |$$    $$< $$    |   
 $$$$$$$ | $$$$$$  |        /$$/           $$$$$$  |$$ |  $$ |$$$$$$$  |$$$$$/    
/  \__$$ |$$ \__$$ |       /$$/  __       /  \__$$ |$$ \__$$ |$$ |  $$ |$$ |_____ 
$$    $$/ $$    $$/       /$$/  /  |      $$    $$/ $$    $$/ $$ |  $$ |$$       |
 $$$$$$/   $$$$$$/        $$/   $$/        $$$$$$/   $$$$$$/  $$/   $$/ $$$$$$$$/ 
                                                                                  
                                                                                  
                                                                                  
             _______   ________  ________                                         
            /       \ /        |/        |                                        
            $$$$$$$  |$$$$$$$$/ $$$$$$$$/                                         
            $$ |__$$ |$$ |__       $$ |                                           
            $$    $$< $$    |      $$ |                                           
            $$$$$$$  |$$$$$/       $$ |                                           
            $$ |__$$ |$$ |_____    $$ |                                           
            $$    $$/ $$       |   $$ |                                           
            $$$$$$$/  $$$$$$$$/    $$/ By: MCyberkid
'''
    print(ban2)


def fetch():
    #url = "https://footballpredictions.net/pt/bet-of-the-day?from=telegram"
    url = "https://www.footballsuper.tips/football-accumulators-tips/football-tips-daily-accumulator/"
    page = browser.open(url)
    page_content = page.read()
    anim("\033[1;32m[+]===============================================[+]\n")
    anim("\033[1;36m  \============= Prediction For Today ============/\n")
    scrap(page_content)


banner()
fetch()
