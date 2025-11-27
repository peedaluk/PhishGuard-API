import models , schemas , database
from models import models
from fastapi import FastAPI , Depends , HTTPException
from sqlalchemy.orm import Session
import joblib, re
import numpy as np
from train_model import get_features

app = FastAPI()

try:
    model = joblib.load("phish_model.pkl")
    print("[+] Model loaded successfully!")
except:
    print("[-] Error: phish_model.pkl not found. Make sure you ran train_model.py")
    model = None


database.Base.metadata.create_all(bind = database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/scan", response_model = schemas.UrlResponse)

def scan_url(Url : schemas.Url , db : Session = Depends(get_db)):
    
    if model is None:
        raise HTTPException(status_code=503, detail="Model not available")
    
    features = get_features(Url.url)
    features = features.reshape(1, -1)
    
    prediction_val = model.predict(features)[0]
    prediction_prob = model.predict_proba(features)[0][1]
    
    prediction_str = "malicious" if prediction_val == 1 else "safe"

    scan_result = models.ScanResult(url = Url.url,prediction = prediction_str,confidence = float(prediction_prob))

    db.add(scan_result)
    db.commit()
    db.refresh(scan_result)
    return scan_result
