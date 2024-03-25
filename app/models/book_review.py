from pydantic import BaseModel, Field
from typing import Optional
from typing_extensions import Annotated


class Review(BaseModel):
    id: int
    text_review: str
    rating: Optional[Annotated[int, Field(ge=0, le=5)]]


class BookReview(BaseModel):
    book_id: int
    review_id: int
