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

def getInfo(url: str, sites_dict: dict):
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    description = soup.find_all('div', class_='kf-det-content')
    title = soup.select_one('.kf-title.kf-det-title.h3.my-4').text
    print(title)
    # sites_dict[title] = {'name': title}

    content: str = ""
    for section in description:
        for element in section.find_all('p'):
            content += element.get_text()
            content += '\n'


    info = soup.find('div', class_=['kf-SideContent', 'aside-content']).find_all(class_="item")
    with open("chiayi_" + sys.argv[2] + ".txt", mode='a', encoding='utf-8') as f:
        f.write('\n\n')
        f.write(info[0].find('span').text)
        f.write(': ')
        f.write(info[0].find('a').text)
        f.write('\n')
        openingElement = soup.find('ul', class_="openingHours_content")
        if openingElement is None:
            f.write(info[-2].find('span').text)
            f.write(': ')
            f.write(info[-2].find('a').get('href'))
            f.write('\n')
            f.write(info[-1].find('span').text)
            f.write(': ')
            f.write(info[-1].find('a').text)
            f.write('\n\n\n\n\n\n')
        else:
            f.write("開放時間: ")
            openingHour = openingElement.find_all('li')
            for opening in openingHour:
                f.write(opening.text)
            f.write('\n')
            f.write(info[3].find('span').text)
            f.write(': ')
            f.write(info[3].find('a').get('href'))
            f.write('\n')
            f.write(info[4].find('span').text)
            f.write(': ')
            f.write(info[4].find('a').text)
            f.write('\n\n\n\n\n\n')
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

    sites_dict = dict()
    for card in cards:
        getInfo(card, sites_dict)

    # with open("chiayi_" + sys.argv[2] + ".txt", mode='a', encoding='utf-8') as f:



if __name__ == "__main__":
    main()
