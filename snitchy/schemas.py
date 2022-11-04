from pydantic import BaseModel
from datetime import date

class Car(BaseModel):
    name:str
    plate:str
    user_id: int
    cartype: str
    
    class Config():
        orm_mode = True

class Ticket(BaseModel):
    subject:str
    pub_date:date
    description:str
    user_id: int
    
    
    class Config():
        orm_mode = True
        

class User(BaseModel):
    name:str
    email:str
    number:str
    