from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.database import SessionLocal
from src.model.orderitems import OrderItem
from src.schemas.user1 import OrderItemBase

Order_item1 = APIRouter(tags=["ORDER_ITEMS"])

db = SessionLocal()

@Order_item1.post("/orderitems/", response_model=OrderItemBase)
def create_orderitem(orderitem: OrderItemBase):
    db_orderitem = OrderItem(

    order_id = orderitem.order_id,
    product_id = orderitem.product_id,
    quantity = orderitem.quantity,
    price = orderitem.price,
    discount = orderitem.discount,
    subtotal = orderitem.subtotal,


    )
    db.add(db_orderitem)
    db.commit()
    return db_orderitem



@Order_item1.get("/orderitems/{orderitem_id}", response_model=OrderItemBase)
def get_orderitem(orderitem_id: str):
    orderitem = db.query(OrderItem).filter(OrderItem.id == orderitem_id).first()
    if not orderitem:
        raise HTTPException(status_code=404, detail="Order item not found")
    return orderitem




@Order_item1.get("/orderitems/", response_model=list[OrderItemBase])
def get_all_orderitems():
    orderitems = db.query(OrderItem).all()
    return orderitems




@Order_item1.put("/orderitems/{orderitem_id}", response_model=OrderItemBase)
def update_orderitem(orderitem_id: str, orderitem: OrderItemBase):
    db_orderitem = db.query(OrderItem).filter(OrderItem.id == orderitem_id).first()
    if not db_orderitem:
        raise HTTPException(status_code=404, detail="Order item not found")
    
    db_orderitem.order_id = orderitem.order_id,
    db_orderitem.product_id = orderitem.product_id,
    db_orderitem.quantity = orderitem.quantity,
    db_orderitem.price = orderitem.price,
    db_orderitem.discount = orderitem.discount,
    db_orderitem.subtotal = orderitem.subtotal,
    
    db.commit()
    return db_orderitem




@Order_item1.delete("/orderitems/{orderitem_id}")
def delete_orderitem(orderitem_id: str):
    db_orderitem = db.query(OrderItem).filter(OrderItem.id == orderitem_id).first()
    if not db_orderitem:
        raise HTTPException(status_code=404, detail="Order item not found")
    db.delete(db_orderitem)
    db.commit()
    return {"message": "Order item deleted successfully"}
