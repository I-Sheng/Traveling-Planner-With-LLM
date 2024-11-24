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
    table = {}
    food_table = loadJson("food/table.json")
    sites_table = loadJson("sites/table.json")

    mergeTable = {**food_table, **sites_table}

    print(len(mergeTable))
    dumpJson(mergeTable, "table.json")

if __name__ == "__main__":
    main()
