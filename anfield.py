# import libraries
import urllib.request

# set options to be headless, ..
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

from bs4 import BeautifulSoup
import pandas as pd
import re
import datetime
import requests
import sys

column_headings=['Date','Home-Team','Away-Team','Attendance', 'Season']
df = pd.DataFrame()
year = 1992
url_list = ["http://lfcstats.co.uk/19921993attendances.html",
"http://lfcstats.co.uk/19931994attendances.html",
"http://lfcstats.co.uk/19941995attendances.html",
"http://lfcstats.co.uk/19951996attendances.html",
"http://lfcstats.co.uk/19961997attendances.html",
"http://lfcstats.co.uk/19971998attendances.html",
"http://lfcstats.co.uk/19981999attendances.html",
"http://lfcstats.co.uk/19992000attendances.html",
"http://lfcstats.co.uk/20002001attendances.html",
"http://lfcstats.co.uk/20012002attendances.html",
"http://lfcstats.co.uk/20022003attendances.html",
"http://lfcstats.co.uk/20032004attendances.html",
"http://lfcstats.co.uk/20042005attendances.html",
"http://lfcstats.co.uk/20052006attendances.html",
"http://lfcstats.co.uk/20062007attendances.html",
"http://lfcstats.co.uk/20072008attendances.html",
"http://lfcstats.co.uk/20082009attendances.html",
"http://lfcstats.co.uk/20092010attendances.html",
"http://lfcstats.co.uk/20102011attendances.html",
"http://lfcstats.co.uk/20112012attendances.html",
"http://lfcstats.co.uk/20122013newattendances.html",
"http://lfcstats.co.uk/20132014newattendances.html",
"http://lfcstats.co.uk/20142015newattendances.html",
"http://lfcstats.co.uk/20152016newattendances.html",
"http://lfcstats.co.uk/20162017newattendances.html",
"http://lfcstats.co.uk/20172018newattendances.html",
"http://lfcstats.co.uk/20182019newattendances.html"]

#This is for testing a single entry
#url_list = ["http://lfcstats.co.uk/19921993attendances.html"]

hdr = { 'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0' }
wd = webdriver.Chrome('chromedriver',options=options)


for url in url_list:
    print("grabbing: ", url)
    """ Selenium method"""
    wd.get(url)
    page = wd.page_source
    soup = BeautifulSoup(page, 'html.parser')
    data=[] 
    table = soup.find("table")
    #items = soup.findAll("li")

    if len(table) < 1:
        print(table)
        print("Didnt find any items so breaking")
        break
    else:

        for row in table.findAll('tr'):
            col = row.findAll('td')
            date = col[0].getText()
            home = col[1].getText()
            away = col[2].getText()
            attendance = col[3].getText()
            #attendance = attendance.strip(',.\nAttendance')
            attendance = ''.join(c for c in attendance if c.isdigit())
            season = str(year)+' '+str(year+1)
            print(season)
            rows = (date, home, away, attendance, season)
            data.append(rows)
        #print(data)
    df = df.append(data,ignore_index=True)
    
    year = year + 1
df.columns = column_headings

df.to_csv('Anfield-Attendance-durty.csv', index=False)