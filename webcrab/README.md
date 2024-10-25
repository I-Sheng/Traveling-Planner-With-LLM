# 嘉義資訊蒐集

## 目標
`/webcrab` 目標是從嘉義市官方觀光網站 [嘉義市觀光旅遊網](https://travel.chiayi.gov.tw/)、及 Google map API 蒐集關於景點、美食及住宿的資訊(景點名稱、景點描述、景點圖片、景點開放時間)。

## 使用方式

### Python 腳本
您可以使用提供的 Python 腳本，從網站上收集特定的資訊。

**指令語法：**
```bash
python3 chiayi_webcrab.py [資訊的第一頁網址] [資訊類型]
```

**範例：**
若要蒐集景點相關資訊，請執行：
```bash
python3 chiayi_webcrab.py https://travel.chiayi.gov.tw/TravelInformation/C000005/1 sites
```

### Bash 腳本
若想快速蒐集關於景點、美食及住宿的綜合資訊，可以使用內建的 bash 腳本。收集包含網站訊息，及景點名稱。

**指令語法：**
```bash
bash script.sh
```

### 從 Google Map 取得 Opening time

**指令語法**
```
python3 get_opening.py chiayi_food_title.txt food
python3 get_opening.py chiayi_sites_title.txt sites
```

### 將各種 Data 合併
* `merge.py` 合併景點資訊
* `add_site_time` 將沒有 opening time 的資料補全

**指令語法**
```
python3 merge.py
python3 add_site_time.py
```
