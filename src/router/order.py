from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.database import SessionLocal
from src.model.orders import Order
from src.schemas.user1 import OrderBase

Order1 = APIRouter(tags=["ORDERS"])

db = SessionLocal()


@Order1.post("/orders/", response_model=OrderBase)
def create_order(order: OrderBase):
    db_order = Order(

    customer_name = order.customer_name,
    order_date = order.order_date,
    status = order.status,    
    total_amount = order.total_amount,
    payment_method = order.payment_method,
    shipping_address = order.shipping_address,
    delivery_date = order.delivery_date,


    )

    db.add(db_order)
    db.commit()
    return db_order

@Order1.get("/orders/{order_id}", response_model=OrderBase)
def get_order(order_id: str):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@Order1.get("/orders/", response_model=list[OrderBase])
def get_all_orders():
    orders = db.query(Order).all()
    return orders

@Order1.put("/orders/{order_id}", response_model=OrderBase)
def update_order(order_id: str, order: OrderBase):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    

    db_order.customer_name = order.customer_name,
    db_order.order_date = order.order_date,
    db_order.status = order.status,    
    db_order.total_amount = order.total_amount,
    db_order.payment_method = order.payment_method,
    db_order.shipping_address = order.shipping_address,
    db_order.delivery_date = order.delivery_date,

    db.commit()
    return db_order

@Order1.delete("/orders/{order_id}")
def delete_order(order_id: str):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(db_order)
    db.commit()
    return {"message": "Order deleted successfully"}
