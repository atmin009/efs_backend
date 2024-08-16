from datetime import datetime  # ใช้ datetime จาก Python เองสำหรับเวลาปัจจุบัน
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean, DateTime  # นำเข้า Boolean และ DateTime จาก SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Building(Base):
    __tablename__ = 'building'
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, index=True)
    name = Column(String, index=True)
    area = Column(String, index=True)

class Unit(Base):
    __tablename__ = 'unit'
    id = Column(Integer, primary_key=True, index=True)
    years = Column(Integer)
    month = Column(Integer)
    amount = Column(Integer)
    idBuilding = Column(Integer, ForeignKey('building.id'))

class NumberOfUsers(Base):
    __tablename__ = 'numberOfUsers'
    id = Column(Integer, primary_key=True, index=True)
    years = Column(Integer)
    month = Column(Integer)
    amount = Column(Integer)

class ExamStatus(Base):
    __tablename__ = 'examStatus'
    id = Column(Integer, primary_key=True, index=True)
    years = Column(Integer)
    month = Column(Integer)
    status = Column(Boolean)

class SemesterStatus(Base):
    __tablename__ = 'semesterStatus'
    id = Column(Integer, primary_key=True, index=True)
    years = Column(Integer)
    month = Column(Integer)
    status = Column(Boolean)

class Member(Base):
    __tablename__ = 'member'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    fname = Column(String)
    lname = Column(String)
    email = Column(String)
    phone = Column(String)
    status = Column(Integer)





class PredictionTable(Base):
    __tablename__ = "predictiontable"

    id = Column(Integer, primary_key=True, index=True)
    building = Column(String, index=True)
    area = Column(Float)
    prediction = Column(Float)
    unit = Column(Float)
    modelName = Column(String)
    month_current = Column(Integer)
    year_current = Column(Integer)
    month_predict = Column(Integer)
    year_predict = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)