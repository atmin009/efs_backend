from sqlalchemy.orm import Session
from typing import List
import pandas as pd
import pickle
from models import Building, ExamStatus, NumberOfUsers, SemesterStatus, Unit
from schemas import PredictionRequest, PredictionResponse
import logging
from fastapi import HTTPException
import os
from datetime import datetime
from fastapi import Query



# --------- ส่วนของการเก็บ log ---------------
# สร้างโฟลเดอร์ 'log' หากยังไม่มี
if not os.path.exists('log'):
    os.makedirs('log')

# สร้างชื่อไฟล์ที่มีวันที่และเวลาปัจจุบัน
current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
log_filename = f'log/log-{current_time}.txt'

# กำหนดค่าให้กับ logging
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(message)s')

# --------- ส่วนของการเก็บ log ---------------

def load_model(model_name: str):
    model_path = f"models/{model_name}.pkl"
    if not os.path.exists(model_path):
        logging.error(f"Model file does not exist: {model_path}")
        raise HTTPException(status_code=404, detail="Model file not found")
    with open(model_path, "rb") as f:
        return pickle.load(f)

def predict(request: PredictionRequest, db: Session) -> List[PredictionResponse]:
    model_name = request.modelName
    
    if not model_name:
        logging.error("Model name is missing or empty")
        raise HTTPException(status_code=400, detail="Model name is required")
    
    model_names = []
    if model_name == "All":
        model_names = [f"T{i}" for i in range(1, 13)]
    else:
        model_names = model_name.split(",")  # แก้ให้ถูกต้องตาม format "T1,T2,T3"

    logging.info(f"Model names to be used: {model_names}")
    
    year = request.year
    month = request.month

    units = db.query(Unit.idBuilding).filter_by(years=year, month=month).distinct().all()
    if not units:
        logging.warning(f"No buildings found in Unit table for year: {year}, month: {month}")
        raise HTTPException(status_code=404, detail="No buildings found for the specified year and month")

    building_ids = [unit.idBuilding for unit in units]
    
    predictions = []

    for building_id in building_ids:
        building = db.query(Building).filter_by(id=building_id).first()
        if not building:
            logging.warning(f"Building not found for id: {building_id}")
            continue

        building_code = building.code
        building_area = building.area

        current_unit = db.query(Unit).filter_by(years=year, month=month, idBuilding=building_id).first()
        unit_amount = current_unit.amount if current_unit else 0

        data = {
            "month": month,
            "building": str(building_id),
            "Area": building_area,
            "Unit": unit_amount
        }

        current_number_of_users = db.query(NumberOfUsers).filter_by(years=year, month=month).first()
        current_exam_status = db.query(ExamStatus).filter_by(years=year, month=month).first()
        current_semester_status = db.query(SemesterStatus).filter_by(years=year, month=month).first()

        data["Eusers"] = current_number_of_users.amount if current_number_of_users else 0
        data["exam"] = current_exam_status.status if current_exam_status else 0
        data["semester"] = current_semester_status.status if current_semester_status else 0

        for i in range(1, 12):
            prev_month = (month - i - 1) % 12 + 1
            prev_year = year - (1 if month - i <= 0 else 0)
            
            number_of_users = db.query(NumberOfUsers).filter_by(years=prev_year, month=prev_month).first()
            exam_status = db.query(ExamStatus).filter_by(years=prev_year, month=prev_month).first()
            semester_status = db.query(SemesterStatus).filter_by(years=prev_year, month=prev_month).first()
            unit = db.query(Unit).filter_by(years=prev_year, month=prev_month, idBuilding=building_id).first()

            data[f"Eusers-{i}"] = number_of_users.amount if number_of_users else 0
            data[f"exam-{i}"] = exam_status.status if exam_status else 0
            data[f"semester-{i}"] = semester_status.status if semester_status else 0
            data[f"Unit-{i}"] = unit.amount if unit else 0

        columns = ['month', 'building', 'Area', 'Eusers'] + \
                  [f'Eusers-{i}' for i in range(1, 12)] + \
                  ['exam'] + \
                  [f'exam-{i}' for i in range(1, 12)] + \
                  ['semester'] + \
                  [f'semester-{i}' for i in range(1, 12)] + \
                  ['Unit'] + \
                  [f'Unit-{i}' for i in range(1, 12)]
        df = pd.DataFrame([data])
        X = df[columns]

        logging.info(f"Building: {building_id}, Data: {data}")
        logging.info(f"DataFrame columns: {X.columns.tolist()}")
        logging.info(f"DataFrame data: {X.values.tolist()}")

        for i, model_name in enumerate(model_names):
            try:
                model = load_model(model_name)
                prediction = model.predict(X)[0]

                # คำนวณ month_predict และ year_predict
                month_predict = (month + i) % 12 + 1
                year_predict = year + (month + i - 1) // 12

                predictions.append({
                    "building": str(building_id),
                    "area": building_area,
                    "prediction": prediction,
                    "unit": unit_amount,
                    "modelName": model_name,
                    "month_current": month,
                    "year_current": year,
                    "month_predict": month_predict,
                    "year_predict": year_predict
                })
                
                logging.info(f"Model: {model_name}, Building: {building_id}, Prediction: {prediction}, Month Predict: {month_predict}, Year Predict: {year_predict}")
            except Exception as model_error:
                logging.error(f"Model prediction error for building {building_id} with model {model_name}: {str(model_error)}")
                raise HTTPException(status_code=500, detail="Model prediction error")
    
    return predictions

