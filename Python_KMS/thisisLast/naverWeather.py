import ssl
import urllib 
from bs4 import BeautifulSoup 
import urllib.request as req

context = ssl._create_unverified_context() 
webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8',context=context)
soup = BeautifulSoup(webpage, 'html.parser') 

# 온도
temps = soup.find('div','temperature_text')
temps = temps.text.strip()
temps = temps[5:7]

info = soup.find('dl','summary_list')

# 체감온도
htemp = info.text.strip()
htemp = htemp[3:7]

# 습도
humidity = info.text.strip()
humidity = humidity[12:14]

# 바람
wind = info.text.strip()
wind = wind[24]