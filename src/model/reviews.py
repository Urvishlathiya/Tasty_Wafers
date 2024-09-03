from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey
from database.database import Base
from datetime import datetime
import uuid

class Review(Base):
    __tablename__ = "reviews"
    id = Column(String(50), primary_key=True, default=str(uuid.uuid4()))
    product_id = Column(String(50), ForeignKey("products.id"), nullable=False)
    customer_name = Column(String(100), nullable=False)
    rating = Column(Integer, nullable=False)
    review_text = Column(String(500), nullable=True)
    review_date = Column(DateTime, default=datetime.now)
    is_approved = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean, default=True)
