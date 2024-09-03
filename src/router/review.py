from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.database import SessionLocal
from src.model.reviews import Review
from src.schemas.user1 import ReviewBase

Review1 = APIRouter(tags=["REVIWES"])


db = SessionLocal()

@Review1.post("/reviews/", response_model=ReviewBase)
def create_review(review: ReviewBase):
    db_review = Review(
    
    product_id = review.product_id,
    customer_name = review.customer_name,
    rating = review.rating,
    review_text = review.review_text,
    review_date = review.review_date

    )
    db.add(db_review)
    db.commit()
    return db_review

@Review1.get("/reviews/{review_id}", response_model=ReviewBase)
def get_review(review_id: str):
    review = db.query(Review).filter(Review.id == review_id).first()
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review

@Review1.get("/reviews/", response_model=list[ReviewBase])
def get_all_reviews():
    reviews = db.query(Review).all()
    return reviews

@Review1.put("/reviews/{review_id}", response_model=ReviewBase)
def update_review(review_id: str, review: ReviewBase):
    db_review = db.query(Review).filter(Review.id == review_id).first()
    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")
    
    db_review.product_id = review.product_id,
    db_review.customer_name = review.customer_name,
    db_review.rating = review.rating,
    db_review.review_text = review.review_text,
    db_review.review_date = review.review_date

    db.commit()
    return db_review

@Review1.delete("/reviews/{review_id}")
def delete_review(review_id: str):
    db_review = db.query(Review).filter(Review.id == review_id).first()
    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")
    db.delete(db_review)
    db.commit()
    return {"message": "Review deleted successfully"}
