# 嘉義資訊蒐集
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/I-Sheng/Traveling-Planner-With-LLM/blob/main/webcrab/README.en.md)

## 目標
`/webcrab` 目標是從嘉義市官方觀光網站 [嘉義市觀光旅遊網](https://travel.chiayi.gov.tw/) 蒐集關於景點、美食及住宿的資訊。

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
若想快速蒐集關於景點、美食及住宿的綜合資訊，可以使用內建的 bash 腳本。

**指令語法：**
```bash
bash script.sh
```

## 快速資訊蒐集
`script.sh` 檔案會自動化蒐集景點、美食及住宿資訊的過程，並將結果彙整至 "chiayi.txt" 檔案中。
