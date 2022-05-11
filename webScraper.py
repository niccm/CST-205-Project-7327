import requests
import json
from bs4 import BeautifulSoup

# Website
url = 'https://www.weatherbug.com/weather-forecast/now/marina-ca-93933'
# Response of website
response = requests.get(url)
# Html
print('\n\n\n\n\n\n\n\n\n\n\n\n\n')
soup = BeautifulSoup(response.text, "lxml")
print(soup)
# # Finds all images
# links = soup.findAll('img')

print(response)
# # If ok, then this
# if response != 200:
#     # Print all img links
#     # print("works")
#     for link in links:
#         #print image source
#         print(link['src'])


