from fastapi import FastAPI, HTTPException, APIRouter , Depends , Header
from database.database import SessionLocal
from src.model.user import User
from src.model.otp import Otp
from src.model.categories import Category
from passlib.context import CryptContext
from src.schemas.user1 import StuBase
from src.utils.otp import generate_otp,send_otp_email
from src.schemas.user1 import Categories


#from src.schemas.student import RollStu, BranchStu
Category1 = APIRouter(tags=["CATEGORIES"])


db = SessionLocal()



@Category1.post("/categories/", response_model= Categories)
def trains_details(category : Categories):
    newDetail = Category(

    user_name = category.user_name,
    types = category.types,
    description = category.description,
    )

    db.add(newDetail)
    db.commit()

    return category


@Category1.get("/get_category_details", response_model=Categories)

def read_details(category_id : str):
    breakpoint()
    details = db.query(Category).filter(Category.id == category_id, Category.is_active==True , Category.is_deleted == False).first()
    if details is None:
        raise HTTPException(status_code=404, detail="Details not found")
    return details


@Category1.get("/all_details/", response_model=list[Categories])
def read_details():
    details = db.query(Category).filter(Category.is_active==True , Category.is_deleted==False).all()
    length_list = len(details)
    if length_list == 0:
        raise HTTPException(status_code=404, detail="Table is empty")
    return details



@Category1.put("/Update_category_details/", response_model=Categories)
def update_details(category_id: str , category : Categories):
    db_detail = db.query(category).filter(category.id == category_id).first()
    if db_detail is None:
        raise HTTPException(status_code=404, detail="Details not found")


    
    db_detail.user_name = category.user_name,
    db_detail.types = category.types,
    db_detail.description = category.description,
    


    db.delete(db_detail)
    db.commit()
    
    
    return db_detail

