import bs4 as bs
import requests 
from requests import get
import urllib.request
import re
from selenium import webdriver
import csv
import pandas as pd

chromedriver = "C:\\Users\\grayson\\Downloads\\chromedriver_win32\\chromedriver.exe"
d = webdriver.Chrome(chromedriver)

classes = ['position','car-number', 'driver', 'final-status', 'points not-mobile']

d.get('https://www.nascar.com/results/race_center/2018/monster-energy-nascar-cup-series/pocono-400/stn/race/')

sauce = bs.BeautifulSoup(d.page_source, 'lxml')
raceStats = sauce.find_all('div', {'class':'table-row'})
race = sauce.find_all('div', {'class':'raceDataTable active dataTable'})


new_data = [ [ [c.text for c in b.find_all('div', {'class':re.compile('|'.join(classes))})] for b in i.find_all('div', {'class':'table-row'})] for i in race]
new_data = new_data[0]

results = 'C:\\Users\\grayson\\Documents\\project-folder\\python\\nascar\\nascar.csv'

with open(results, 'w') as dataFile:
    writer = csv.writer(dataFile)
    writer.writerows([new_data][0])


# df = pd.read_csv(results, sep=',', names= ['currentPosition','carNumber', 'driver', 'status', 'points'])
# print(df)





