from fastapi import APIRouter
import database, schemas, models,hashing,oauth2
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
# from ..repository import user
from typing import List

# router = APIRouter(
#     prefix="/user",
#     tags=['Users']
# )

# get_db = database.get_db

# @router.post('/user')
# def create_user(request:schemas.User,db:Session = Depends(get_db)):
#     hashedPassword = pwd_context.hash(request.password)
#     new_user = models.User(name=request.name,email=request.email,password=hashing.Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user
    
    
# @router.get('/user/{id}',status_code=200,response_model=List[schemas.User])
# def showuser(id,db:Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         # response.status_code = statuss.HTTP_404_NOT_FOUND
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog {id} unavailable")

#     return user


# from fastapi import APIRouter
# from .. import database, schemas, models
# from sqlalchemy.orm import Session
# from fastapi import APIRouter,Depends,status
import repository.user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User,db: Session = Depends(get_db)):
    return repository.user.create(request,db)

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return repository.user.show(id,db)