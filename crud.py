from fastapi import APIRouter,Depends,HTTPException
from schemas import CreateTask,UpdateTask,TaskResponse
from db import get_db
from sqlalchemy.orm import Session
from typing import List
from models import Todo
from fastapi.responses import JSONResponse


router= APIRouter()


@router.get('/view')
def get_task(db:Session = Depends(get_db)):
    return db.query(Todo).all()


@router.post('/create',response_model=TaskResponse)
def create_task(task:CreateTask, db:Session = Depends(get_db)):
    new_task = Todo(
        id= task.id,
        task_name= task.task_name,
        task_description=task.task_description,
        status=task.status
    )
    
    db.add(new_task)
    db.commit()
    return new_task

@router.delete('/delete/{id}')
def delete_task(id:int, db:Session = Depends(get_db)):

    db_task= db.query(Todo).filter(id == Todo.id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found.")

    db.delete(db_task)
    db.commit()

    return JSONResponse(status_code=200, content={"message":"Task deleted Successfully"})

@router.get('/view/{id}')
def get_task_byId(id:int, db:Session = Depends(get_db)):
    db_task= db.query(Todo).filter(id == Todo.id).first()

    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return db_task

@router.put('/update/{id}', response_model=TaskResponse)
def update_task(id:int , task:UpdateTask , db:Session = Depends(get_db)):
    db_task= db.query(Todo).filter(id == Todo.id).first()

    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    updated_task = task.model_dump(exclude_unset=True)

    for k,v in updated_task.items():
        setattr(db_task,k,v)
    
    db.commit()
    db.refresh(db_task)

    return db_task

    
    
    