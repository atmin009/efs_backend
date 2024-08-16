from pydantic import BaseModel

class BuildingCreate(BaseModel):
    code: str
    name: str
    area: str

class UnitCreate(BaseModel):
    years: int
    month: int
    amount: int
    idBuilding: int

class NumberOfUsersCreate(BaseModel):
    years: int
    month: int
    amount: int

class ExamStatusCreate(BaseModel):
    years: int
    month: int
    status: bool

class SemesterStatusCreate(BaseModel):
    years: int
    month: int
    status: bool

class MemberCreate(BaseModel):
    username: str
    password: str
    fname: str
    lname: str
    email: str
    phone: str
    status: int

class PredictionRequest(BaseModel):
    year: int
    month: int
    modelName: str

class PredictionResponse(BaseModel):
    building: str
    area: float
    prediction: float
    unit: float
    modelName: str
    month_current: int
    year_current: int
    month_predict: int
    year_predict: int
    
class LoginData(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    user_id: int
    username: str
    status: int
    name: str
