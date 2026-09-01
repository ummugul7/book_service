from typing import List
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
import models
import schemas
from database import Base, engine, get_db

# Tabloları oluştur
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book Service API")

@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "healthy"}

@app.post("/books", response_model=schemas.BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(title=book.title, author=book.author)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/books", response_model=List[schemas.BookResponse], status_code=status.HTTP_200_OK)
def get_books(db: Session = Depends(get_db)):
    books = db.query(models.Book).all()
    return books