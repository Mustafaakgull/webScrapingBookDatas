import requests
from bs4 import BeautifulSoup
import pandas as pd

books = []
for i in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    response = requests.get(url)
    response = response.text
    soup = BeautifulSoup(response, 'html.parser')
    ol = soup.find('ol')
    articles = ol.find_all('article', class_='product_pod')

    for article in articles:
        image = article.find('img')
        title = image.attrs['alt']
        star = article.find('p')
        star = star['class'][1]
        price = article.find('p', class_='price_color')
        price = float(price.text[2:])
        books.append([title, price, star])


page = pd.DataFrame(books, columns=['title', 'price', 'star'])
page.to_csv('books.csv')

