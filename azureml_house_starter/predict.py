
from pathlib import Path
import joblib
import pandas as pd

ROOT = Path(__file__).parent

# 載入訓練好的模型
model = joblib.load(ROOT / 'outputs/house_price_model.joblib')

# 自動取得模型類型
model_type = type(model.named_steps['model']).__name__

model_names = {
    'LinearRegression': '線性迴歸',
    'RandomForestRegressor': '隨機森林'
}

model_name = model_names.get(model_type, model_type)

print('========== 房價預測 ==========')
print(f'目前使用模型：{model_name}')

# 建立要預測的房屋資料
new_house = pd.DataFrame([{
    '坪數': 35,
    '屋齡': 10,
    '距捷運公里': 1.2,
    '房間數': 3,
    '區域': '住宅區'
}])

print('\n輸入房屋資料：')
print(new_house.to_string(index=False))

# 進行房價預測
pred = float(model.predict(new_house)[0])

print('\n========== 預測結果 ==========')
print(f'使用模型：{model_name}')
print(f'預測房屋總價：{pred:,.1f} 萬元')
print('注意：資料為模擬資料，僅供教學使用')
