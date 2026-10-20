
from pathlib import Path
import json
import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

ROOT = Path(__file__).parent
DATA = ROOT / 'houses_demo.csv'

TARGET = '總價萬元'
NUM = ['坪數', '屋齡', '距捷運公里', '房間數']
CAT = ['區域']

# 讀取資料
df = pd.read_csv(DATA, encoding='utf-8-sig').dropna(subset=[TARGET])

X = df[NUM + CAT]
y = df[TARGET]

# 切分訓練集與測試集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 建立模型 Pipeline
def make_pipeline(regressor):
    preprocess = ColumnTransformer([
        ('num', SimpleImputer(strategy='median'), NUM),
        ('cat', Pipeline([
            ('fill', SimpleImputer(strategy='most_frequent')),
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ]), CAT),
    ])

    return Pipeline([
        ('preprocess', preprocess),
        ('model', regressor)
    ])


# 訓練與比較模型
scores = {}
best_model = None
best_model_name = None
best_mae = float('inf')

models = [
    ('線性迴歸', LinearRegression()),
    ('隨機森林', RandomForestRegressor(
        n_estimators=150,
        random_state=42,
        min_samples_leaf=2
    ))
]

print('========== 開始模型訓練 ==========')

for name, regressor in models:

    pipeline = make_pipeline(regressor)

    # 訓練模型
    pipeline.fit(X_train, y_train)

    # 預測測試集
    pred = pipeline.predict(X_test)

    # 評估模型
    mae = float(mean_absolute_error(y_test, pred))
    rmse = float(mean_squared_error(y_test, pred) ** 0.5)
    r2 = float(r2_score(y_test, pred))

    metric = {
        'MAE_萬元': round(mae, 2),
        'RMSE_萬元': round(rmse, 2),
        'R2': round(r2, 4)
    }

    scores[name] = metric

    print(f'\n模型：{name}')
    print(f'MAE  ：{mae:.2f} 萬元')
    print(f'RMSE ：{rmse:.2f} 萬元')
    print(f'R²   ：{r2:.4f}')

    # 依照 MAE 選擇最佳模型（越小越好）
    if mae < best_mae:
        best_mae = mae
        best_model = pipeline
        best_model_name = name


# 儲存最佳模型
out = ROOT / 'outputs'
out.mkdir(exist_ok=True)

joblib.dump(best_model, out / 'house_price_model.joblib')

# 儲存評估結果
(out / 'metrics.json').write_text(
    json.dumps(scores, ensure_ascii=False, indent=2),
    encoding='utf-8'
)

print('\n========== 模型訓練完成 ==========')
print(f'最終選用模型：{best_model_name}')
print(f'最佳 MAE：{best_mae:.2f} 萬元')
print('模型已儲存：outputs/house_price_model.joblib')
print('評估結果已儲存：outputs/metrics.json')
