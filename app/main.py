from fastapi import FastAPI

from .routes import book
from .routes import book_review

app = FastAPI()

app.include_router(book.router)
app.include_router(book_review.router)
