# routers/product.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.model.product import Product
from src.schemas.user1 import Products
from database.database import SessionLocal

router = APIRouter(tags=["Products"])


db = SessionLocal()

@router.post("/products/", response_model=Products)
def create_product(product: Products):
    new_product = Product(
    name = product.name,
    description = product.description,
    price = product.price,
    category = product.category,              
    )
    db.add(new_product)
    db.commit()
    return new_product

@router.get("/products/{product_id}", response_model=Products)
def get_product(product_id: str):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.get("/products/", response_model=list[Products])
def get_all_products():
    return db.query(Product).all()

@router.put("/products/{product_id}", response_model=Products)
def update_product(product_id: str, product: Products):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    
    db_product.name = product.name,
    db_product.description = product.description,
    db_product.price = product.price,
    db_product.category = product.category,

    
    db.commit()
    return db_product

@router.delete("/products/{product_id}", response_model=Products)
def delete_product(product_id: str):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return db_product
