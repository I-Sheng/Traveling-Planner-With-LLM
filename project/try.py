import re
import json

# Function to process the opening hours string and format it
def process_hours(hours_string):
    # Replace "公休" with None
    hours_string = hours_string.replace("公休日", "None")
    # Replace "24小時營業" with "00:00-24:00"
    hours_string = hours_string.replace("24小時營業", "00:00-24:00")
    
    # Parse each day and its hours
    hours_dict = {}
    days = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    for day in days:
        match = re.search(rf"{day}\s*(\d{2}:\d{2}\s*~\s*\d{2}:\d{2}|None)", hours_string)
        if match:
            hours_dict[day] = match.group(1)
    
    return hours_dict

# Sample input (assuming this data is extracted from the file)
data = """
KANO遊客中心
服務時間：星期一 08:00 ~ 17:00 星期二 08:00 ~ 17:00 星期三 08:00 ~ 17:00 星期四 08:00 ~ 17:00 星期五 08:00 ~ 17:00 星期六 08:00 ~ 17:00 星期日 08:00 ~ 17:00

嘉義製材所
開放時間：星期一 None 星期二 None 星期三 09:00 ~ 17:00 星期四 09:00 ~ 17:00 星期五 09:00 ~ 17:00 星期六 09:00 ~ 17:00 星期日 09:00 ~ 17:00

大溪厝水環境教育園區
開放時間：星期一 00:00 ~ 24:00 星期二 00:00 ~ 24:00 星期三 00:00 ~ 24:00 星期四 00:00 ~ 24:00 星期五 00:00 ~ 24:00 星期六 00:00 ~ 24:00 星期日 00:00 ~ 24:00
"""

# Process the data
places = {}
place_entries = data.strip().split("\n\n\n")
for entry in place_entries:
    lines = entry.split("\n")
    place_name = lines[0].strip()
    hours_string = " ".join(lines[1:])
    places[place_name] = process_hours(hours_string)

# Output to JSON
output_file = 'opening_hours.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(places, f, ensure_ascii=False, indent=4)

print(f"Data has been written to {output_file}.")
