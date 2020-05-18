from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('https://yandex.ru/')
html = req.read()

soup = BeautifulSoup(html, 'html.parser')
news = soup.find_all('a', class_='home-link list__item-content list__item-content_with-icon home-link_black_yes')

results = {}
for item in news:
    title = item.find('span', class_='news__item-content').get_text(strip=True)
    href = item.get('href')
    results[title] = href

for title, href in results.items():
    print(title)
    print(href)

f = open('news.txt', 'w', encoding='utf-8')
i = 1
for title, href in results.items():
    f.write(f'Новость № {i}\nНазвание: {title}\nСсылка: {href}\n*******************\n')
    i += 1
f.close()