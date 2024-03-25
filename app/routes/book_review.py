from fastapi import APIRouter
from typing import List

from ..models.book_review import Review


router = APIRouter()

mock_review_db = [
    {"id": 1, "text_review": "ABC", "rating": 5},
    {"id": 2, "text_review": "PQR", "rating": 5},
    {"id": 3, "text_review": "LMN", "rating": 5},
]


@router.get("/reviews/", response_model=List[Review])
async def read_reviews():
    """Get all reviews"""
    return mock_review_db
