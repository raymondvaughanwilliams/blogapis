from fastapi import APIRouter,Depends,status,Response ,HTTPException
import schemas, database ,models,oauth2
from typing import List
from sqlalchemy.orm import Session
import repository.blog


router = APIRouter(tags=['Blog'])


    
get_db = database.get_db

@router.get('/blogs', response_model=  List[schemas.ShowBlog])
def all(db:Session = Depends(database.get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    blogs = db.query(models.Blog).all()
    # blogs = models.Blog.query.all()
    return repository.blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return repository.blog.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return repository.blog.destroy(id,db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return repository.blog.update(id,request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return repository.blog.show(id,db)