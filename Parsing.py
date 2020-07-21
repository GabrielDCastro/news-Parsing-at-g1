from bs4 import BeautifulSoup
import requests

url =  'http://g1.com.br'
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                        ' AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/84.0.4147.89 Safari/537.36'}

req = requests.get(url, headers=header)
html = req.text



soup = BeautifulSoup(html, 'html.parser')

colection = soup.find_all(class_='feed-post-link gui-color-primary gui-color-hover') #this class is used in every post
dolar = soup.find(class_='post-economia-cotacao__quote-value')

for item in colection:
    print(item.get_text(), "\n")