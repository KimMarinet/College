import requests
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib as mpl
import matplotlib.pyplot as plt

def weather_func2():
    url = "https://www.weather.go.kr/w/obs-climate/land/city-obs.do"
    source = requests.get(url)
    soup = BeautifulSoup(source.content,"html.parser", from_encoding='utf-8')
    table = soup.find('table', {'class':'table_develop3'})

    data = []

    for tr in table.find_all('tr'):
        # table_data 리스트 생성
        tds = list(tr.find_all('td'))
        for td in tds:
            if td.find('a'):
                area = td.find('a').text
                temp = tds[5].text
                if(tds[7].text == '\xa0'):
                    hum_temp = tds[5].text
                else:
                    hum_temp = tds[7].text
                humidity = tds[10].text
                # middle Test
                print("{0:<7} {1:<7} {2:<7} {3:<7} {4:<7}".format(area,temp,hum_temp,humidity))
                data.append([area,temp,hum_temp,humidity])

weather_func2()
