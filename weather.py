import pandas as pd
import requests
from bs4 import BeautifulSoup
page = requests.get('https://weather.com/weather/tenday/l/c15a3a656efc30cdeb88720c60282137be4a73cae1d9826d0f068502424f7344')

#get beautifulsoup obj
soup = BeautifulSoup(page.content,'html.parser')
tenDayData = soup.find(id = 'twc-scrollabe')
days = tenDayData.find_all( class_ = 'clickable closed')

#as you loop through the days, get the day name, descriptions, precipitation, wind, humidity
dayNames = [oneDay.find(class_ = 'date-time').get_text() for oneDay in days]
dayDescriptions = [oneDay.find(class_ = 'description').get_text() for oneDay in days]
dayPrecip = [oneDay.find(class_ = 'precip').get_text() for oneDay in days]
dayWind = [oneDay.find(class_ = 'wind').get_text() for oneDay in days]
dayHumidity = [oneDay.find(class_ = 'humidity').get_text() for oneDay in days]

#Data frame takes a dictionary
weather = pd.DataFrame(
    {
        'Day': dayNames,
        'Descriptions': dayDescriptions,
        'Precipitation': dayPrecip,
        'Wind': dayWind,
        'Humidity': dayHumidity,
    })

print(weather)
weather.to_csv('weather.csv')
weather.to_json('weather.json')