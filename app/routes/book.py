from fastapi import APIRouter
from typing import List

from ..models.book import Book


router = APIRouter()

mock_book_db = [
    {"id": 1, "title": "ABC", "author": "XYZ", "publication_year": 2020},
    {"id": 2, "title": "PQR", "author": "MBP", "publication_year": 2021},
    {"id": 3, "title": "LMN", "author": "RDJ", "publication_year": 2022},
]


@router.get("/books/", response_model=List[Book])
async def read_books():
    ''' Get all Books '''
    return mock_book_db
