from datetime import datetime
import os
import googlemaps
import math

#from urllib.parse import urlparse, parse_qsl
from dotenv import load_dotenv

load_dotenv()


class DistanceMatrix():  # Extend unittest.TestCase
    def __init__(self, *args, **kwargs):
        super(DistanceMatrix, self).__init__(*args, **kwargs)  # Initialize superclass
        self.key = os.getenv('GOOGLE_MAP_API_KEY')  # Load API key from .env
        self.client = googlemaps.Client(key=self.key)

    def testAllParams(self, ls):
        # Real request to the Google Distance Matrix API

        origins = ls
        destinations = ls

        now = datetime.now()

        # manual site: https://developers.google.com/maps/documentation/distance-matrix/distance-matrix?hl=zh-tw
        matrix = self.client.distance_matrix(
            origins,
            destinations,
            mode="driving",
            language="zh-TW",
            avoid="tolls",
            units="imperial",
            departure_time=now,
            traffic_model="pessimistic",
        )

        # Print the real API response
        #print(matrix, type(matrix))
        return matrix

    def matrixTo2dArray(self, sites: list):
        matrix = self.testAllParams(sites)
        neglect = []
        for i in range(len(matrix['destination_addresses'])):
            if matrix['destination_addresses'][i] == '':
                neglect.append(i)

        arr = []
        for i in range(len(matrix['rows'])):
            if i in neglect:
                continue
            tmp = []
            src = matrix['rows'][i]

            for j in range(len(src['elements'])):
                if j in neglect:
                    continue
                dist = src['elements'][j]
                # print(dist)
                if 'duration_in_traffic' in dist:
                    minutes:int = math.ceil(dist['duration_in_traffic']['value'] / 60)
                    minutes += (10 - (minutes % 10))
                    tmp.append(minutes)
                else:
                    print("No duration_in_traffic in the element, something go wrong!")
                    tmp.append(1441)
            arr.append(tmp)


        return [sites[i] for i in range(len(matrix['destination_addresses'])) if matrix['destination_addresses'][i] != ''], arr


def travel_time(sites: list):
    # print(sites)
    distance_matrix = DistanceMatrix()
    exist_sites, arr = distance_matrix.matrixTo2dArray(sites)
    # print('successfully get the 2d array!')
    # for ele in arr:
    #     for i in ele:
    #         print(i, end=' ')
    #     print()
    return exist_sites, arr

if __name__ == "__main__":
    distance_matrix = DistanceMatrix()
    sites: list = [
        "嘉義公園",
        "檜意森活村",
        "蒜頭糖廠",
        ]
    arr = distance_matrix.matrixTo2dArray(sites)
    for ele in arr:
        for i in ele:
            print(i, end=' ')
        print()

