import requests
import sys
from bs4 import BeautifulSoup
import re
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}



def getPage(url: str, pages: list):
    pages.append(url)
    print("curent URL: ", url)
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    nextPageElement = soup.find('li', class_='kf-paginator-NextPage')
    if nextPageElement is None:
        return
    nextUrl = "https://travel.chiayi.gov.tw" + nextPageElement.find('a').get('href')
    getPage(nextUrl, pages)
    return


def getSite(url: str):
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    cards = soup.find_all('div', class_='card-col')
    return ["https://travel.chiayi.gov.tw" + card.find('a').get('href') for card in cards]

def getInfo(url: str):
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    description = soup.find_all('div', class_='kf-det-content')
    with open("chiayi_" + sys.argv[2] + ".txt", mode='a', encoding='utf-8') as f:
        title = soup.select_one('.kf-title.kf-det-title.h3.my-4').text
        print(title)
        f.write(title)
        f.write('\n')
        for des in description:
            f.write(des)
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

    cards = []
    for page in pages:
        cards += getSite(page)
    for card in cards:
        getInfo(card)




if __name__ == "__main__":
    main()
