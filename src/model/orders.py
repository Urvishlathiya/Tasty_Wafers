from sqlalchemy import Column, String, Float, DateTime
from database.database import Base
from datetime import datetime
import uuid

class Order(Base):
    __tablename__ = "orders"
    id = Column(String(50), primary_key=True, default=str(uuid.uuid4()))
    customer_name = Column(String(100), nullable=False)
    order_date = Column(DateTime, default=datetime.now)
    status = Column(String(20), nullable=False)
    total_amount = Column(Float, nullable=False)
    payment_method = Column(String(50), nullable=False)
    shipping_address = Column(String(200), nullable=False)
    delivery_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
