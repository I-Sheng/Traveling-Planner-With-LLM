import requests
import sys
from bs4 import BeautifulSoup
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}


from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def download_image(url, save_path):
    try:
        # Define headers to mimic a browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }

        # Configure the retry strategy
        retry_strategy = Retry(
            total=5,  # Total number of retry attempts
            backoff_factor=1,  # Wait 1s, 2s, 4s, etc. between retries
            status_forcelist=[429, 500, 502, 503, 504],  # HTTP status codes to retry on
            allowed_methods=["HEAD", "GET", "OPTIONS"]  # Updated parameter name
        )

        # Create an adapter with the retry strategy
        adapter = HTTPAdapter(max_retries=retry_strategy)

        # Create a session and mount the adapter for both HTTP and HTTPS
        session = requests.Session()
        session.mount("https://", adapter)
        session.mount("http://", adapter)

        # Send the GET request with headers and a timeout
        print('Sending request...')
        response = session.get(url, headers=headers, stream=True, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        # Write the content to a file in chunks
        print('Opening file...')
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:  # Ensure that the chunk is not empty
                    file.write(chunk)

        print(f"Image successfully downloaded: {save_path}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # e.g., 404 Not Found
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")  # e.g., DNS failure, refused connection
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")  # Request timed out
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")  # Any other requests exceptions
    except Exception as err:
        print(f"An unexpected error occurred: {err}")  # Other exceptions

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

    # openingElement = soup.find('ul', class_="openingHours_content")
    # if openingElement is None:
        # content += info[-2].find('span').text + ': ' + info[-2].find('a').get('href') + '\n' + info[-1].find('span').text + ': ' + info[-1].find('a').text + '\n\n\n\n\n\n'
    # else:
        # content += "開放時間: "
        # openingHour = openingElement.find_all('li')
        # for opening in openingHour:
           # content += opening.text
        # content += '\n' + info[3].find('span').text + ': ' + info[3].find('a').get('href') + '\n' + info[4].find('span').text + ': ' + info[4].find('a').text + '\n\n\n\n\n\n'

    tab1 = soup.find('div', id='tab-1')

    # if tab1 == None:

    img_tags = tab1.find_all('img')
    img_urls = [ "https://travel.chiayi.gov.tw" + img['src'] for img in img_tags if 'src' in img.attrs]
    if img_tags is not None:
        download_image(img_urls[0], f'picture/{title}.jpg')

    return {'name': title, 'content': content}





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
