# 等候時間的模型比較

在旅遊規劃中，停留時間的預測對於行程安排至關重要，其中包括對景點和餐廳停留時間的估計。由於資料量的考量，本專案以餐廳的停留時間預測作為模型訓練的基礎。

## 停留時間的預測模型
我們希望透過模型預測停留時間的上下限。為避免同時預測上下限導致模型收斂至非最佳值，我們分別使用 `model1` 預測下限，`model2` 預測上限。

### 資料來源
停留時間的數據來自 Google API 提供的 `populartimes`，用於預測餐廳的等候時間。模型選用包括 CNN、RNN、GRU 和 LSTM，並以 Mean Absolute Error（MAE）作為 Loss function 來比較各模型的性能。

## 損失函數（Loss Function）
1. **MAE**: 使用 PyTorch 的 L1 loss 作為基準。
1. Q Error: 
q<sub>error</sub> = |p - q| / q
其中，`p` 為預測值，`q` 為真實值。

## 模型性能比較

模型訓練目標為預測餐廳的等候時間，以 MAE 評估模型性能。下表中展示了每個模型的 `model1`（下限）與 `model2`（上限）的測試 MAE loss 和 Q loss 以及對應的 epoch。

| Model    | Version | Best MAE Loss | Epoch of Best MAE | Best Q Loss | Epoch of Best Q |
| -------- | ------- | ------------- | ----------------- | ----------- | --------------- |
| **CNN**  | model1  | 13.9163       | 75                | 0.3780      | 81              |
|          | model2  | 26.0074       | 85                | 0.4995      | 53              |
| **RNN**  | model1  | 13.4247       | 130               | 0.3534      | 130             |
|          | model2  | 27.2800       | 928               | 0.4866      | 890             |
| **GRU**  | model1  | 14.9047       | 99                | 0.3865      | 54              |
|          | model2  | 30.2178       | 84                | 0.4879      | 60              |
| **LSTM** | model1  | 14.6243       | 1825              | 0.3841      | 1833            |
|          | model2  | 36.4877       | 1629              | 0.5095      | 281             |
* 我們最後選擇 RNN 的 model 來預測我們的停留時間上限，因為它在 model1, model2 裡均 Q loss 最小
## 模型 Code

- [GRU 模型代碼](https://colab.research.google.com/drive/1EdBMtwskH62YuKUllwOkzP5mXTN1yZBe?usp=sharing)
- [LSTM 模型代碼](https://colab.research.google.com/drive/1sALbzUHX_04mqT4WX4AHy13H21vctoh0?usp=sharing)
- [RNN 模型代碼](https://colab.research.google.com/drive/1ntiwLf7wpDGFm7hlah1YTZtEV0hzrvTA?usp=sharing)
- [CNN 模型代碼](https://colab.research.google.com/drive/1Y5g_BWPK-AIgD9gtE9SQFj0OTxJIxwpv?usp=sharing)

## 新模型設計（newModel2）

為了提升 `model2` 的準確性，我們將 `model1`（下限）的預測結果與 `populartimes` 數據結合，作為 newModel2（上限）的輸入。

### newModel2 模型與 model2 比較

| Model    | Version   | Best Loss | Epoch of Best Loss | Best Q Loss | Epoch of Best Q Loss |
| -------- | --------- | --------- | ------------------ | ----------- | -------------------- |
| **RNN**  | model2    | 27.2800   | 928                | 0.4866      | 890                  |
|          | newModel2 | 27.0163   | 273                | 0.4682      | 138                  |
| **GRU**  | model2    | 30.2178   | 84                 | 0.4879      | 60                   |
|          | newModel2 | 31.6792   | 76                 | 0.4752      | 12                   |
| **LSTM** | model2    | 36.4877   | 1629               | 0.5095      | 281                  |
|          | newModel2 | 31.1202   | 218                | 0.4752      | 49                   |
* 我們最後選擇 RNN 的 newModel2 來預測我們的停留時間上限，因為她的Q loss 最小
## newModel2 Code

- [newModel2_RNN](https://colab.research.google.com/drive/1A41-HbKuhHhpkzfwtj6Aquuf_CHa10bC?usp=sharing)
- [newModel2_GRU](https://colab.research.google.com/drive/1mMaPH6UVIoYmOsAe5Kx2lawdCpHZ_ADT?usp=sharing)
- [newModel2_LSTM](https://colab.research.google.com/drive/1oFqsdrmMJPP93IabW7WCTEwBIro_0LZj?usp=sharing)
