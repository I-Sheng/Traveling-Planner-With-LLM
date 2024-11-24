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
    table = loadJson("table.json")
    print(table)

if __name__ == "__main__":
    main()
