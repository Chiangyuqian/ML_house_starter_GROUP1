# ML房價預測_GROUP#

**注意：** `houses_demo.csv` 是人為生成的模擬資料，與真實房市無關。模型的評估結果不能用來宣稱真實房價預測能力。

## 執行環境

- Python 3.12（含）以上
- 支援 Windows、macOS
- 所需套件請參考 `requirements.txt`

執行前請確認 Python 版本：

```bash
python --version
```

macOS 若使用 `python3` 指令，則執行：

```bash
python3 --version
```

## 本機操作

### 1. 建立虛擬環境

Windows：
```powershell
python -m venv .venv
```

macOS：
```bash
python3 -m venv .venv
```

### 2. 啟用虛擬環境

Windows（PowerShell）：
```powershell
.\.venv\Scripts\Activate.ps1
```

若 PowerShell 限制執行指令碼，請先執行：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

再重新啟用虛擬環境。

macOS：
```bash
source .venv/bin/activate
```

### 3. 安裝套件

啟用虛擬環境後，Windows 與 macOS 均執行：

```bash
python -m pip install -r requirements.txt
```

### 4. 執行程式

Windows 與 macOS 均執行：

```bash
python make_demo_data.py
python train.py
python predict.py
```

### 5. 離開虛擬環境

Windows 與 macOS 均執行：

```bash
deactivate
```

## 檔案說明

- `make_demo_data.py`：產生房價模擬資料。
- `houses_demo.csv`：示範資料。欲換成真實資料，請保留欄位 `坪數,屋齡,距捷運公里,房間數,區域,總價萬元`，並在 `train.py` 修改資料路徑。
- `train.py`：資料缺值處理、類別編碼、80/20 分割，比較線性迴歸與隨機森林，依 MAE 選擇最佳模型，輸出 MAE、RMSE、R² 等評估結果。
- `predict.py`：載入最佳模型並預測新房屋總價（萬元）。
- `requirements.txt`：專案所需 Python 套件。

## 輸出結果

程式執行後，結果會儲存在 `outputs` 資料夾：

- `house_price_model.joblib`：訓練完成的最佳模型。
- `metrics.json`：模型評估結果。
- `模型訓練結果.xlsx`：記錄模型訓練時間、資料筆數、MAE、RMSE、R²，以及最終選擇的最佳模型。
- `房價預測結果.xlsx`：記錄房屋輸入資料、預測總價及使用的模型。

**備註：** 首次執行需建立虛擬環境並安裝套件，之後只需啟用虛擬環境即可執行程式。建立虛擬環境前，請確認使用的 Python 為 3.12（含）以上。
