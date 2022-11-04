from fastapi import FastAPI,Depends, status , Response ,HTTPException
from pydantic import BaseModel
# from .schemas import  Blog
import  models,schemas,hashing
from database import engine,SessionLocal ,get_db
from sqlalchemy.orm import Session
from typing import List
# from  .routers import blog, user, authentication
from passlib.context import CryptContext
from routers import blog,user , authentication

app = FastAPI()

 
app.include_router(blog.router)
app.include_router(authentication.router)
app.include_router(user.router)

models.Base.metadata.create_all(engine)







 

pwd_context = CryptContext(schemes=['bcrypt'],deprecated="auto")    
