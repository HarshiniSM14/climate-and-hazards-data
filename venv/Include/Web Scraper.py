import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996#.YMye2-gzY2w')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')
items = week.find_all(class_='tombstone-container')
#print(items[0].find(class_='Period-name').get_text())
#print(items[0].find(class_='Short-desc').get_text())
#print(items[0].find(class_='Temp').get_text())

Period_names = [item.find(class_='period-name').get_text() for item in items]
Short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
Temperatures = [item.find(class_='temp').get_text() for item in items]
#print(Period_names)
#print(Short_descriptions)
#print(Temperatures)

Climate_stuff = pd.DataFrame({
                              'Period': Period_names,
                              'Short_descriptions': Short_descriptions,
                              'Temperatures': Temperatures
                            })
print(Climate_stuff)
Climate_stuff.to_csv('Climate and Hazards data.csv')
