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

def merge(prefix: str):
    opening_file = f'{prefix}_opening_hours.json'
    file = f'chiayi_{prefix}.json'
    opening_data = loadJson(opening_file)
    data = loadJson(file)
    for key in list(data.keys()):
        if key not in opening_data:
            print(f"Warning: {key} not found in {prefix}_opening_hours.json")
            data.pop(key)
            continue

        if 'opening_hours' in opening_data[key]['result']:
            data[key]['opening_hours'] = opening_data[key]['result']['opening_hours']['weekday_text']
        else:
            print(f"Warning: 'opening_hours' not found for key: {key}")
            data.pop(key)

    dumpJson(data, f'{prefix}.json')

def main():

    merge('food')
    merge('sites')

if __name__ == "__main__":
    main()

