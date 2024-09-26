#!/bin/bash

python3 chiayi_webcrab.py https://travel.chiayi.gov.tw/TravelInformation/C000005/1 sites
python3 chiayi_webcrab.py https://travel.chiayi.gov.tw/TravelInformation/C000005/2 food
python3 chiayi_webcrab.py https://travel.chiayi.gov.tw/TravelInformation/C000005/3 hotel

cat chiayi_sites.txt chiayi_food.txt chiayi_hotel.txt > chiayi.txt
