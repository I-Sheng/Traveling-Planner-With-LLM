import requests
import sys
from bs4 import BeautifulSoup
import re
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}



def getPage(url: str, pages: list):
    if url.endswith('javascript:void(0)'):
        return
    pages.append(url)
    print("curent URL: ", url)
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    nextPageElement = soup.find('div', class_='next-blk').find('a', class_='next-page')
    if nextPageElement.get('href') is None:
        return
    nextUrl = "https://www.twtainan.net" + nextPageElement.get('href')
    getPage(nextUrl, pages)
    return


def getSite(url: str):
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    cardList = soup.find('ul', class_='info-card-list')
    cards = cardList.find_all('li', class_='item')
    # print('after card')
    # print('type(cards)', type(cards))
    # print('len(cards)', len(cards))
    # print('cards', cards)
    for card in cards:
        with open("tainan_" + 'food' + ".txt", mode='a', encoding='utf-8') as f:
            title = card.find('a', class_='link').get('title')
            print(title)
            f.write(title)
            f.write('\n')
            f.close()



def main():
    argv = sys.argv

    pages: list = []
    if len(argv) < 2:
        print("Please input URL of the first page and its fileName")
        return
    elif len(argv) > 3:
        print("Please give only two argument")
        return
    else:
        getPage(argv[1], pages)
    print(f'pages size: {len(pages)}')

    cards = []
    for page in pages:
        getSite(page)




if __name__ == "__main__":
    main()
