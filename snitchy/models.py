from sqlalchemy import Column, Integer, String, ForeignKey,DateTime
from database import Base
from sqlalchemy.orm import relationship
import datetime as datetime


class Ticket(Base):
    __tablename__ = 'tickets'
    
    __seachbale__ = ['name','description']
    id = Column(Integer, primary_key=True)
    subject = Column(String)
    color = Column(String, nullable=True)
    pub_date = Column(DateTime, nullable=False,default=datetime.datetime.utcnow)
    description = Column(String(255), nullable= True)
    car_number = Column(String(255), nullable= True)
    car_type = Column(String(255), nullable= True)
    # assigned_to = Column(Integer, ForeignKey('users.id'),nullable=True)

    users = relationship('User', back_populates="tickets")
    bills = relationship('Bill', back_populates="tickets")

    # category_id = Column(Integer, ForeignKey('category.id'),nullable=False)
    # category = relationship('Category',backref=backref('category', lazy=True))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="tickets")
    # user_id = Column(Integer, ForeignKey('users.id'),nullable=False)
    # userr = relationship('User',backref=backref('users', lazy=True))

    image_1 = Column(String(150), nullable=True, default='image1.jpg')
    image_2 = Column(String(150), nullable=True, default='image2.jpg')
    image_3 = Column(String(150), nullable=True, default='image3.jpg')




class User(Base): 
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    number = Column(String)
    curr_bill = Column(String)

    tickets = relationship('Ticket', back_populates="users")
    
    
class Bill(Base):
    __tablename__ = 'bills'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    tickets = relationship('Ticket', back_populates="bills")
    amount = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))
    ticket_id = Column(Integer, ForeignKey('tickets.id'))