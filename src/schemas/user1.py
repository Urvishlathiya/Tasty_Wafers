from pydantic import BaseModel 
from datetime import datetime

class StuBase(BaseModel):
    user_name : str
    Mobile_No : int
    Email : str
    Date_of_Birth : str
    password : str
    Gender : str

class User_OTP(BaseModel):
    Email : str
    
class OTP_Verify(BaseModel):
    Email : str
    otp : str

class Categories(BaseModel):
    user_name : str
    types : str
    description : str

class Products(BaseModel):
    name  : str
    description : str
    price : str
    category  : str

class InventoryBase(BaseModel):
    product_id: str
    quantity: int
    location: str
    restock_threshold: int
    restock_date: datetime

class OrderBase(BaseModel):
    customer_name: str
    order_date: datetime
    status: str
    total_amount: float
    payment_method: str
    shipping_address: str
    delivery_date: datetime

class OrderItemBase(BaseModel):
    order_id: str
    product_id: str
    quantity: int
    price: float
    discount: float
    subtotal: float

class ReviewBase(BaseModel):
    product_id: str
    customer_name: str
    rating: int
    review_text: str
    review_date: datetime


