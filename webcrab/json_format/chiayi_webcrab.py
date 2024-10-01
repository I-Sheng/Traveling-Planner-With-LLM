import requests
import sys
from bs4 import BeautifulSoup
import json

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
    title = soup.select_one('.kf-title.kf-det-title.h3.my-4').text
    print(title)

    content: str = ""
    for section in description:
        for element in section.find_all('p'):
            content += element.get_text() + '\n'


    info = soup.find('div', class_=['kf-SideContent', 'aside-content']).find_all(class_="item")
    content += '\n\n' + info[0].find('span').text + ': ' + info[0].find('a').text + '\n'

    openingElement = soup.find('ul', class_="openingHours_content")
    if openingElement is None:
        content += info[-2].find('span').text + ': ' + info[-2].find('a').get('href') + '\n' + info[-1].find('span').text + ': ' + info[-1].find('a').text + '\n\n\n\n\n\n'
    else:
        content += "開放時間: " 
        openingHour = openingElement.find_all('li')
        for opening in openingHour:
           content += opening.text
        content += '\n' + info[3].find('span').text + ': ' + info[3].find('a').get('href') + '\n' + info[4].find('span').text + ': ' + info[4].find('a').text + '\n\n\n\n\n\n'

    tab1 = soup.find_all('div', id='tab-1')

    if tab1 == None:
        return {'name': title, 'content': content}
    
    img_tags = tab1.find_all('img')
    img_urls = [img['src'] for img in img_tags if 'src' in img.attrs]
    return {'name': title, 'content': content, 'images': img_urls}
    



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
        dict_item = getInfo(card)
        sites_dict[dict_item['name']] = dict_item

    with open("chiayi_" + sys.argv[2] + ".json", mode='w', encoding='utf-8') as json_file:
        json.dump(sites_dict, json_file, indent=4)



if __name__ == "__main__":
    main()
