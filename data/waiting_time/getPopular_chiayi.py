import os
import sys
import json
import populartimes

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GOOGLE_MAP_API_KEY') #Load API key from .env

def dumpDict(data: list, file_path: str):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def loadList(file_path: str):
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



def getSiteData(placeIdList, name):
    target :dict = {}
    # print("length of placeId is", len(placeIdList))
    for placeId in placeIdList:
        data = populartimes.get_id(API_KEY, placeId)
        if target == {}:
            target = data
        elif "populartimes" not in data:
            continue
        elif "populartimes" not in target:
            target = data
        else:
            targetSum :int = 0
            dataSum :int = 0
            for i in range(7):
                targetSum += sum(target["populartimes"][i]['data'])
                dataSum += sum(data["populartimes"][i]['data'])
            if dataSum > targetSum:
                target = data
    if "populartimes" in target:
        if "time_spent" in target:
            popular_timeSpent = loadList("popular_timeSpent.json")
            popular_timeSpent[name] = target
            dumpDict(popular_timeSpent, "popular_timeSpent.json")
        else:
            popular_notimeSpent = loadList("popular_notimeSpent.json")
            popular_notimeSpent[name] = target
            dumpDict(popular_notimeSpent, "popular_notimeSpent.json")
    else:
        if "time_spent" in target:
            nopopular_timeSpent = loadList("nopopular_timeSpent.json")
            nopopular_timeSpent[name] = target
            dumpDict(nopopular_timeSpent, "nopopular_timeSpent.json")
        else:
            nopopular_notimeSpent = loadList("nopopular_notimeSpent.json")
            nopopular_notimeSpent[name] = target
            dumpDict(nopopular_notimeSpent, "nopopular_notimeSpent.json")





def main():
    argv = sys.argv
    listFile: str = "items"
    if len(argv) != 3:
        print("Only inclue listOfName and Prefix")
        return
    elif len(argv) == 3:
        listFile:str = argv[1]
        prefix: str = argv[2]
        # Open a file in read mode
    dumpDict({}, "chiayi_{prefix}_nopopular_notimeSpent.json")
    dumpDict({}, "chiayi_{prefix}_popular_notimeSpent.json")
    dumpDict({}, "chiayi_{prefix}_nopopular_timeSpent.json")
    dumpDict({}, "chiayi_{prefix}_popular_timeSpent.json")

    with open(listFile, 'r') as file:
        for line in file:
            line = line.strip()
            placeIdList, name = getPlaceId(line)
            if placeIdList == 'error':
                continue
            getSiteData(placeIdList, name)
            print(f'{name} complete execute')



if __name__ == "__main__":
    main()

