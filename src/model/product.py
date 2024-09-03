from sqlalchemy import Column, String, Boolean, DateTime, Float, Integer
from database.database import Base
from datetime import datetime
import uuid

class Product(Base):
    __tablename__ = "products"
    id = Column(String(50), primary_key=True, default=str(uuid.uuid4()))
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(String, nullable=False)
    category = Column(String(50), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
