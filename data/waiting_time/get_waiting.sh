#!/bin/bash
cp ../webcrab/*.title.txt webcrab
python getPopular_chiayi.py webcrab/chiayi_sites_title.json
mv *.json dictData/sites
python getPopular_chiayi.py webcrab/chiayi_food_title.json
mv *.json dictData/food
cd dictData/food
python table.py
cd ../sites
python table.py
cd ..
python merge.py
cd ..
python waiting_time.py
