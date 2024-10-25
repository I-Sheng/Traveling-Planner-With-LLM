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


site_dict = {
        '慈龍寺': [
            "Monday:00:00-24:00",
            "Tuesday:00:00-24:00",
            "Wednesday:00:00-24:00",
            "Thursday:00:00-24:00",
            "Friday:00:00-24:00",
            "Saturday:00:00-24:00",
            "Sunday:00:00-24:00"
            ],
        '蘭潭音樂噴泉': [
            "Monday:19:30-21:40",
            "Tuesday:19:30-21:40",
            "Wednesday:19:30-21:40",
            "Thursday:19:30-21:40",
            "Friday:19:30-21:40",
            "Saturday:19:30-21:40",
            "Sunday:19:30-21:40"
            ],
        '嘉大植物園': [
            "Monday:00:00-24:00",
            "Tuesday:00:00-24:00",
            "Wednesday:00:00-24:00",
            "Thursday:00:00-24:00",
            "Friday:00:00-24:00",
            "Saturday:00:00-24:00",
            "Sunday:00:00-24:00"
            ],
        '嘉義火車站': [
            "Monday:04:50-23:00",
            "Tuesday:04:50-23:00",
            "Wednesday:04:50-23:00",
            "Thursday:04:50-23:00",
            "Friday:04:50-23:00",
            "Saturday:04:50-23:00",
            "Sunday:04:50-23:00"
            ],
        '彌陀映月橋': [
            "Monday:00:00-24:00",
            "Tuesday:00:00-24:00",
            "Wednesday:00:00-24:00",
            "Thursday:00:00-24:00",
            "Friday:00:00-24:00",
            "Saturday:00:00-24:00",
            "Sunday:00:00-24:00"
            ],
        '十二門古砲': [
            "Monday:00:00-24:00",
            "Tuesday:00:00-24:00",
            "Wednesday:00:00-24:00",
            "Thursday:00:00-24:00",
            "Friday:00:00-24:00",
            "Saturday:00:00-24:00",
            "Sunday:00:00-24:00"
            ],
        '埤子頭植物園': [
                "Monday:08:30-16:00",
                "Tuesday:08:30-16:00",
                "Wednesday:08:30-16:00",
                "Thursday:08:30-16:00",
                "Friday:08:30-16:00",
                "Saturday:08:30-16:00",
                "Sunday:08:30-16:00"
                ],
        '蘭潭': [
                "Monday:00:00-24:00",
                "Tuesday:00:00-24:00",
                "Wednesday:00:00-24:00",
                "Thursday:00:00-24:00",
                "Friday:00:00-24:00",
                "Saturday:00:00-24:00",
                "Sunday:00:00-24:00"
                ],
        '劉厝里百年老樹': [
                "Monday:00:00-24:00",
                "Tuesday:00:00-24:00",
                "Wednesday:00:00-24:00",
                "Thursday:00:00-24:00",
                "Friday:00:00-24:00",
                "Saturday:00:00-24:00",
                "Sunday:00:00-24:00"
                ],
        '頂庄社區': [
                "Monday:00:00-24:00",
                "Tuesday:00:00-24:00",
                "Wednesday:00:00-24:00",
                "Thursday:00:00-24:00",
                "Friday:00:00-24:00",
                "Saturday:00:00-24:00",
                "Sunday:00:00-24:00"
                ],
        '丙午震災紀念碑': [
                "Monday:00:00-24:00",
                "Tuesday:00:00-24:00",
                "Wednesday:00:00-24:00",
                "Thursday:00:00-24:00",
                "Friday:00:00-24:00",
                "Saturday:00:00-24:00",
                "Sunday:00:00-24:00"
                ],
        }


def add_data(sites:dict):
    file = 'chiayi_sites.json'
    data = loadJson(file)
    for site, week_time in site_dict.items():
        sites[site] = data[site]
        sites[site]['weekday_text'] = site_dict[site]

    return sites


def merge_json(file1, file2):
    sites = loadJson(file1 + '.json')
    food = loadJson(file2 + '.json')
    sites = add_data(sites)
    merge_dict = {**sites, **food}
    dumpJson(merge_dict, 'sitesData.json')



def main():
    merge_json('sites', 'food')

if __name__ == "__main__":
    main()

