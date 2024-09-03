from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey, Boolean
from database.database import Base
from datetime import datetime
import uuid

class OrderItem(Base):
    __tablename__ = "orderitems"
    id = Column(String(50), primary_key=True, default=str(uuid.uuid4()))
    order_id = Column(String(50), ForeignKey("orders.id"), nullable=False)
    product_id = Column(String(50), ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    discount = Column(Float, nullable=True, default=0.0)
    subtotal = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean, default=True)
