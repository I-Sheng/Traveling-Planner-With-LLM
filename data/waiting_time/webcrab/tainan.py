import requests
import sys
from bs4 import BeautifulSoup
import re
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}



def getSite(url: str):
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    caption_element = soup.find_all('div', class_='info-card-item')
    #print('len of elements: ', len(caption_element))
    for caption in caption_element:
        if caption == None:
            continue

        title = caption.find('h3', class_='info-title').text
        if title == None:
            print('title is None!')
            continue

        with open("tainan_" + sys.argv[1] + ".txt", mode='a', encoding='utf-8') as f:
            print(title)
            f.write(title)
            f.write('\n')
            f.close()
    return

    # cards = soup.find_all('div', class_=['group-list', 'message'])
    # return ["https://tbocc.cyhg.gov.tw/" + card.find('a').get('href') for card in cards]

# def getInfo(url: str):
    # response = requests.get(url, headers=headers)
    # response.encoding = 'utf-8'
    # soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    # # description = soup.find_all('div', class_='kf-det-content')
    # with open("cyhg_" + sys.argv[1] + ".txt", mode='a', encoding='utf-8') as f:
        # title = soup.find('h3').text
        # print(title)
        # f.write(title)
        # f.write('\n')
        # f.close()



def main():
    argv = sys.argv

    pages: list = []
    if len(argv) < 2:
        return
    elif len(argv) > 3:
        return

    # getPage(argv[1], pages)
    pages = [f'https://www.twtainan.net/zh-tw/attractions?sortby=Hits&page={i}' for i in range(1,47)]

    for page in pages:
        getSite(page)




if __name__ == "__main__":
    main()
