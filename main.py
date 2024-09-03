from fastapi import FastAPI
from src.router.user import User1
from src.router.user import Otp_router
from src.router.categories import Category1
from src.router.products import router
from src.router.inventories import Inventory1
from src.router.order import Order1
from src.router.order_item import Order_item1
from src.router.review import Review1


app = FastAPI()
app.include_router(User1)
app.include_router(Otp_router)
app.include_router(Category1)
app.include_router(router)
app.include_router(Inventory1)
app.include_router(Order1)
app.include_router(Order_item1)
app.include_router(Review1)