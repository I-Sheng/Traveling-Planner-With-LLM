# Chiayi Information Gathering

## Goal
This project aims to gather information about sites, food, and hotels in Chiayi from the official [Travel in Chiayi City](https://travel.chiayi.gov.tw/) website.

## Usage

### Python Script
You can use the provided Python script to collect specific information from the website. 

**Command Syntax:**
```bash
python3 chiayi_webcrab.py [first page of the information] [information type]
```

**Example:**
To gather information about sites, run:
```bash
python3 chiayi_webcrab.py https://travel.chiayi.gov.tw/TravelInformation/C000005/1 sites
```

### Bash Script
To quickly gather combined information about sites, food, and hotels, use the included bash script.

**Command Syntax:**
```bash
bash script.sh
```

## Rapid Information Gathering
The `script.sh` file automates the process of retrieving and combining information on sites, food, and hotels into "chiayi.txt".
