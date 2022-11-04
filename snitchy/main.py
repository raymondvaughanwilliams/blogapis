from fastapi import FastAPI,Depends, status , Response ,HTTPException
from pydantic import BaseModel
# from .schemas import  Blog
import  models,schemas
from database import engine,SessionLocal
from sqlalchemy.orm import Session
from typing import List
# from  .routers import blog, user, authentication
from passlib.context import CryptContext
app = FastAPI()
 
models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# app.include_router(authentication.router)
# app.include_router(blog.router)
# app.include_router(user.router)




# @app.post('/car', status_code=status.HTTP_201_CREATED)
# def create(request:schemas.Car,db:Session = Depends(get_db)):
#     new_car = models.Car(title=request.title,body=request.body)
#     db.add(new_car)
#     db.commit()
#     db.refresh(new_car)
#     return new_car


@app.post('/ticket', status_code=status.HTTP_201_CREATED)
def create(request:schemas.Ticket,db:Session = Depends(get_db)):
    new_ticket = models.Ticket(subject=request.subject,description=request.description)
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket


@app.get('/ticket/{id}', status_code=200,response_model=schemas.Ticket)
def create(id, response: Response,db:Session = Depends(get_db)):
    ticket = db.query(models.Ticket).filter(models.Ticket.id == id).first()
    return ticket

@app.get('/tickets',status_code=200,response_model=List[schemas.Ticket])
def alltickets(db:Session = Depends(get_db)):
    tickets = db.query(models.Ticket).all()
    return tickets