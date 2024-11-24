import os
import json

def dumpJson(data: dict, file_path: str):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def loadJson(file_path: str):
    with open(file_path, 'r') as file:
      json_data = file.read()
      data = json.loads(json_data)
    file.close()
    return data

def main():
    opening_data = loadJson("webcrab/sitesData_opening.json")
    waiting_data = loadJson("waiting_time/sitesData_waiting.json")

    print("size of opening", len(opening_data))
    print("size of waiting", len(waiting_data))

    for key in opening_data.keys():
        if key not in waiting_data:
            print(key, "not in waiting_data")


    for key in waiting_data.keys():
        if key not in opening_data:
            print(key, "not in opening_data")


if __name__ == "__main__":
    main()

