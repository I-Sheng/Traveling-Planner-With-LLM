import json
import sys

def analyzeFile(fileName: str):
    with open(fileName, 'r') as file:
        data = json.load(file)
    print("lengh of list is", len(data))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Please specify the city prefix for your analysis.")
    if len(sys.argv) > 3:
        print("Too many arguments, only need two")

    prefix: str = sys.argv[1]

    fileList = ["popular_timeSpent.json", "popular_notimeSpent.json", "nopopular_timeSpent.json", "nopopular_notimeSpent.json"]

    for file in fileList:
        fileName:str = prefix + "_food_" + file
        print("fileName: ",  fileName)
        analyzeFile(fileName)


