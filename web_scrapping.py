import requests
from bs4 import BeautifulSoup

KEYWORDS = {'Kubernetes', 'фото', 'web', 'python'}

r = requests.get('https://habr.com/ru/all/')
r.raise_for_status()

# print(r.text)

articles = BeautifulSoup(r.text, features='html.parser').find_all('article')
for article in articles:
    preview = article.find_all('div', class_='article-formatted-body article-formatted-body_version-1')
    preview_text = {pre.text for pre in preview}
    # print(preview_text)
    # print('-----------')
    if KEYWORDS & preview_text:
        date = articles.find_all('span', class_='tm-article-snippet__datetime-published')
        print(date)

