#!/bin/bash

python3 chiayi_webcrab.py https://travel.chiayi.gov.tw/TravelInformation/C000005/1 sites
python3 chiayi_webcrab.py https://travel.chiayi.gov.tw/TravelInformation/C000005/2 food
python3 chiayi_webcrab.py https://travel.chiayi.gov.tw/TravelInformation/C000005/3 hotel

python3 chiayi_title.py https://travel.chiayi.gov.tw/TravelInformation/C000005/1 sites_title
python3 chiayi_title.py https://travel.chiayi.gov.tw/TravelInformation/C000005/2 food_title
python3 chiayi_title.py https://travel.chiayi.gov.tw/TravelInformation/C000005/3 hotel_title

