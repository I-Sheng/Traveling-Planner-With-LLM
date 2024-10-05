import os
import sys
import json

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GOOGLE_MAP_API_KEY') #Load API key from .env

def dumpDict(data: dict, file_path: str):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def loadDict(file_path: str):
    with open(file_path, 'r') as file:
      json_data = file.read()
      data = json.loads(json_data)
    file.close()
    return data



def parseJson(output:str)-> list:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(current_dir, output)
    if not os.path.exists(json_file_path):
        print(f"File {output} not found.")
        exit()
    with open(json_file_path, 'r') as file:
        json_data = file.read()
    try:
        response_data = json.loads(json_data)
        placeIdList = [response_data['places'][i]['id'] for i in range(len(response_data['places']))]
        # Access the id
        return placeIdList
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        return "error"
    except KeyError:
        print("Key 'places' or 'id' not found in the JSON data.")
        return "error"


def getPlaceId(item:str, output: str = "output.json")-> list:
    item = item + " 嘉義"
    command = f"curl -X POST -d '{{\"textQuery\" : \"{item}\"}}' -H 'Content-Type: application/json' -H 'X-Goog-Api-Key: {API_KEY}' -H 'X-Goog-FieldMask: places.id,places.displayName,places.formattedAddress' 'https://places.googleapis.com/v1/places:searchText' > {output}"

    os.system(command)
#Here is debug Section
    # print(f"The Output of {item}")
    # os.system(f"cat {output}")
    # print("End Output\n\n\n\n\n")
#End debugsection
    placeId = parseJson(output)
    return placeId, item



def getSiteData(name:str, placeIdList:list, file_name:str):
    target :dict = {}
    # print("length of placeId is", len(placeIdList))
    output = 'output.json'
    command = f"curl -L -X GET 'https://maps.googleapis.com/maps/api/place/details/json?place_id={placeIdList[0]}&fields=opening_hours&key={API_KEY}' > {output}"
    os.system(command)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(current_dir, output)
    with open(json_file_path, 'r') as file:
        json_data = file.read()
    try:
        response_data = json.loads(json_data)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        return "error"

    os.system(command)
    opening_hours = loadDict(file_name)
    opening_hours[name] = response_data
    dumpDict(opening_hours, file_name)


def main():
    argv = sys.argv
    listFile: str = "items"
    if len(argv) > 3:
        print("Only inclue listOfName & file_name")
        return
    listFile:str = argv[1]
    file_name:str = f'{argv[2]}_opening_hours.json'

        # Open a file in read mode
    dumpDict({}, file_name)

    with open(listFile, 'r') as file:
        for line in file:
            line = line.strip()
            placeIdList, name = getPlaceId(line)
            if placeIdList == 'error':
                continue
            getSiteData(line, placeIdList, file_name)
            print(f'{name} complete execute')



if __name__ == "__main__":
    main()

