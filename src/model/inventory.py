from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean
from database.database import Base
from datetime import datetime
import uuid

class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(String(50), primary_key=True, default=str(uuid.uuid4()))
    product_id = Column(String(50), ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    location = Column(String(100), nullable=False)
    restock_threshold = Column(Integer, nullable=False)
    restock_date = Column(DateTime, nullable=True)
    last_updated = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
