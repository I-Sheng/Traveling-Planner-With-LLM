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
    prefix = "site"
    path_prefix = "sites"
    table = {}
    data1 = loadJson("popular_timeSpent.json")
    data2 = loadJson("popular_notimeSpent.json")
    data3 = loadJson("nopopular_timeSpent.json")
    data4 = loadJson("nopopular_notimeSpent.json")


    dumpJson(list(data1.values()), f"../../{path_prefix}/chiayi_{prefix}_popular_timeSpent.json")
    dumpJson(list(data2.values()), f"../../{path_prefix}/chiayi_{prefix}_popular_notimeSpent.json")
    dumpJson(list(data3.values()), f"../../{path_prefix}/chiayi_{prefix}_nopopular_timeSpent.json")
    dumpJson(list(data4.values()), f"../../{path_prefix}/chiayi_{prefix}_nopopular_notimeSpent.json")


    mergeList = {**data1, **data2, **data3, **data4}
    for key, value in mergeList.items():
        key = " ".join(key.split(" ")[:-1])
        table[value['name']] = key

    print(len(table))
    dumpJson(table, "table.json")

if __name__ == "__main__":
    main()
