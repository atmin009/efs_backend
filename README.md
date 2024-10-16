![downloads](https://img.shields.io/badge/framework-FAST%20API-green)
![badge](https://img.shields.io/badge/Language-python-blue)


# ระบบพยากรณ์การใช้ไฟฟ้า มหาวิทยาลัยวลัยลักษณ์
ระบบพยากรณ์การใช้ไฟฟ้า มหาวิทยาลัยวลัยลักษณ์ ภายใต้การดำเนินโครงงานการพยากรณ์การใช้ไฟฟ้ารายเดือนของหน่วยการศึกษาโดยใช้เทคนิคการทำเหมืองข้อมูล กรณีศึกษา มหาวิทยาลัยวลัยลักษณ์ ซึ่งเป็นหนึ่งในโปรเจคจบของนักศึกษา หลักสูตรเทคโนโลยีสารสนเทศและนวัตกรรมดิจิตัล (เทคโนโลยีอัจฉริยะ ปัจจุบัน) สาขาวิชาเทคโนโลยีสารสนเทศ สำนักวิชาสารสนเทศศาสตร์ มหาวิทยาลัยวลัยลักษณ์ 

## เกี่ยวกับระบบ
  ระบบพยากรณ์การใช้ไฟฟ้าของมหาวิทยาลัยวลัยลักษณ์ถูกพัฒนาขึ้นโดยใช้โมเดลการเรียนรู้ของเครื่องแบบ GradientBoostingRegressor ซึ่งเป็นหนึ่งในเทคนิคที่มีประสิทธิภาพสูงในตระกูลการเรียนรู้แบบเสริมกำลัง (Boosting) กระบวนการทำงานของโมเดลนี้เริ่มจากการสร้างต้นไม้ตัดสินใจต้นแรกเพื่อทำนายค่า จากนั้นจะค่อยๆ เพิ่มโมเดลใหม่ที่เน้นการแก้ไขข้อผิดพลาดของโมเดลก่อนหน้าในแต่ละรอบการเรียนรู้ ทำให้โมเดลสุดท้ายมีความแม่นยำมากขึ้นเรื่อยๆ
  การนำ GradientBoostingRegressor มาใช้ในการพยากรณ์การใช้ไฟฟ้า ทำให้สามารถทำนายการใช้พลังงานได้อย่างมีประสิทธิภาพ แม้ว่าข้อมูลการใช้พลังงานจะมีความผันผวนในแต่ละช่วงเวลา โมเดลนี้สามารถจัดการกับข้อมูลที่มีความซับซ้อนได้ดี ด้วยการค่อยๆ ปรับปรุงโมเดลแต่ละรอบให้แม่นยำยิ่งขึ้นด้วยแนวทางนี้ ระบบสามารถช่วยลดข้อผิดพลาดในการคาดการณ์การใช้ไฟฟ้า สนับสนุนการบริหารจัดการพลังงานให้มีประสิทธิภาพสูงสุดแก่มหาวิทยาลัย

### `FrontEnd`
- [React Framework](https://github.com/atmin009/efs_frontend)

### `Backend`
- Fast API
  
### `Database`
- [MySQL](https://github.com/atmin009/efs_backend/blob/f9174a0f939eaf84f8bae9964fdeccab93e5b804/Database.sql)
  
## Installation and Commands

| Installation Command                               | Description                           |
|----------------------------------------------------|---------------------------------------|
| `pip install fastapi uvicorn`                      | Install FastAPI and Uvicorn           |
| `pip install sqlalchemy pymysql`                   | Install SQLAlchemy and PyMySQL        |
| `pip install scikit-learn==1.5.0`                  | Install scikit-learn version 1.5.0    |
| `pip install fastapi[all] python-multipart`        | Install FastAPI with all dependencies and python-multipart |
| `pip install fastapi-cors`                         | Install FastAPI CORS                  |
| `pip install bcrypt`                               | Install bcrypt for password hashing   |
| `uvicorn main:app --reload`                        | Run the FastAPI app with Uvicorn      |

### `คู่มือการใช้งานระบบ`
- https://www.youtube.com/playlist?list=PL8zWJ_x1KCtxJe8vBrPdKlLfM8yIL_c1s
  
### `พัฒนาระบบโดย`
- ศุภณัฐ ขุนนุ้ย
- ศิขรินทร์ รักษาชาติ
- เกียรติศักดิ์ ศิริเพ็ชร์

### `Advisor`
- Aj.จักริน วีแก้ว
  
#### `สาขาเทคโนโลยีสารสนเทศและนวัตกรรมดิจิทัล สำนักวิชาสารสนเทศศาสตร์ มหาวิทยาลัยวลัยลักษณ์`



