# Azure ML 房價預測_GROUP#

**注意：** houses_demo.csv 是人為生成的模擬資料，與真實房市無關。模型的評估結果不能用來宣稱真實房價預測能力。

## 本機操作
```bash
python -m pip install -r requirements.txt
python make_demo_data.py
python train.py
python predict.py
```

- `houses_demo.csv`：示範資料。欲換真實資料，請保留欄位 `坪數,屋齡,距捷運公里,房間數,區域,總價萬元`，並在 `train.py` 改資料路徑。
- `train.py`：資料缺值處理、類別編碼、80/20 分割、比較線性迴歸與隨機森林，依 MAE 選模，輸出模型與 MAE/RMSE/R²。
- `predict.py`：載入模型並預測新房屋總價（萬元）。
- `score.py`：Azure ML 線上端點的推論入口，輸入結構見 `sample-request.json`。
- `conda.yml`：Azure 線上部署環境設定。部署需選擇能提供必要運算資源的區域/機型，並確認模型路徑與環境。
