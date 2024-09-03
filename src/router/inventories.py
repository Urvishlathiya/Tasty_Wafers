from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.model.inventory import Inventory
from src.schemas.user1 import InventoryBase
from database.database import SessionLocal

Inventory1 = APIRouter(tags=["INVENTORY"])

db = SessionLocal()

@Inventory1.post("/inventory/", response_model=InventoryBase)
def create_inventory(inventory: InventoryBase):
    db_inventory = Inventory(

    product_id = inventory.product_id,
    quantity = inventory.quantity,
    location = inventory.location,
    restock_threshold = inventory.restock_threshold,
    restock_date = inventory.restock_date,

    )
    db.add(db_inventory)
    db.commit()
    
    return db_inventory

@Inventory1.get("/inventory/{inventory_id}", response_model=InventoryBase)
def get_inventory(inventory_id: str):
    inventory = db.query(Inventory).filter(Inventory.id == inventory_id).first()
    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return inventory

@Inventory1.get("/inventory/", response_model=list[InventoryBase])
def get_all_inventory():
    inventory = db.query(Inventory).all()
    return inventory

@Inventory1.put("/inventory/{inventory_id}", response_model=InventoryBase)
def update_inventory(inventory_id: str, inventory: InventoryBase):
    db_inventory = db.query(Inventory).filter(Inventory.id == inventory_id).first()
    if not db_inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    
    db_inventory.product_id = inventory.product_id,
    db_inventory.quantity = inventory.quantity,
    db_inventory.location = inventory.location,
    db_inventory.restock_threshold = inventory.restock_threshold,
    db_inventory.restock_date = inventory.restock_date,

    db.commit()
    return db_inventory

@Inventory1.delete("/inventory/{inventory_id}")
def delete_inventory(inventory_id: str):
    db_inventory = db.query(Inventory).filter(Inventory.id == inventory_id).first()
    if not db_inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    db.delete(db_inventory)
    db.commit()
    return {"message": "Inventory deleted successfully"}
