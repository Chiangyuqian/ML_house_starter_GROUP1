"""Azure ML Managed Online Endpoint scoring script (joblib model folder)."""
import json
import os
import joblib
import pandas as pd

model = None

def init():
    global model
    model_dir = os.environ['AZUREML_MODEL_DIR']
    model = joblib.load(os.path.join(model_dir, 'house_price_model.joblib'))

def run(raw_data):
    try:
        payload = json.loads(raw_data)
        rows = payload['input_data']
        df = pd.DataFrame(rows)
        result = model.predict(df)
        return {'predictions_萬元': [round(float(v), 2) for v in result]}
    except Exception as exc:
        return {'error': str(exc)}
