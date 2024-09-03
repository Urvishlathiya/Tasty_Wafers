from sqlalchemy import Column,Integer,String,Boolean,DateTime
from database.database import Base
from datetime import datetime
import uuid


class Category(Base):
    __tablename__ = "categories"
    id = Column(String(50), primary_key=True, default=str(uuid.uuid4()))
    user_name = Column(String(20),nullable=False)
    types = Column(String(50),nullable=False)
    description = Column(String(30),nullable=False)
    is_deleted=Column(Boolean,default=False)
    is_active=Column(Boolean,default=True)
    created_at=Column(DateTime,default=datetime.now)
    modified_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)
    is_verified = Column(Boolean , default= False)