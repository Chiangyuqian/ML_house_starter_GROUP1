# Azure ML 房價預測：可執行入門範例

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

## Azure ML Studio（以圖形介面操作）
1. 建立 Azure ML Workspace，開啟 https://ml.azure.com/。
2. 在工作區使用 Notebook/Compute instance，上傳本專案檔案並執行上面的三個 Python 命令。
3. 確認 `outputs/house_price_model.joblib`、`outputs/metrics.json` 已建立。
4. Studio 的 Models 頁面選 Register → From local files，選模型檔 `house_price_model.joblib`（或包含檔案的資料夾）。
5. 在 Endpoints → Real-time endpoints 建立 Managed endpoint，部署時選擇模型、`score.py`、`conda.yml` (以自訂推論環境配置)，選支援的 CPU 機型。
6. 在 Test 分頁以 `sample-request.json` 測試，看到 `predictions_萬元` 才代表端點完成。
7. 展示完請刪除閒置的 Endpoint 與 Compute，避免持續計費。

參考 Microsoft Learn：
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-managed-online-endpoints

**安全提醒：** joblib/pickle 只能載入自己訓練或可信來源的模型；不要下載不明模型直接反序列化。
