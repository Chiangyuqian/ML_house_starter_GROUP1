import numpy as np
import pandas as pd
from pathlib import Path
rng = np.random.default_rng(42)
n = 500
area = rng.uniform(15, 80, n)
age = rng.integers(0, 45, n)
distance = rng.uniform(0.2, 15, n)
rooms = np.clip(np.rint(area / 16 + rng.normal(0, .7, n)), 1, 6).astype(int)
location = rng.choice(['市中心', '住宅區', '郊區'], n, p=[.35, .45, .20])
location_value = pd.Series(location).map({'市中心': 420, '住宅區': 180, '郊區': -90}).to_numpy()
price = 220 + area * 38 - age * 5.8 - distance * 18 + rooms * 22 + location_value + rng.normal(0, 85, n)
price = np.maximum(price, 150).round(1)
df = pd.DataFrame({'坪數':area.round(1), '屋齡':age, '距捷運公里':distance.round(2), '房間數':rooms, '區域':location, '總價萬元':price})
p = Path(__file__).parent / 'houses_demo.csv'
df.to_csv(p, index=False, encoding='utf-8-sig')
print(f'建立示範資料：{p}，共 {n} 筆（模擬數據，非真實房價）')
