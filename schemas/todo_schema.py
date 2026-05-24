from pydantic import BaseModel, Field
from typing import Literal, Optional
from datetime import datetime



class CreateTask(BaseModel):
    id:int
    task_name :str = Field(... , min_length=3, max_length=50)
    task_description: Optional[str] = Field(default=None, max_length=250)
    status: Literal["completed", "running"] = "running"
    created: Optional[datetime] = Field(default_factory=datetime.utcnow)


class UpdateTask(BaseModel):
    task_name:Optional[str] = Field(default=None, min_length=3, max_length=50)
    task_description: Optional[str] = Field(default=None, max_length=500)
    status: Optional[Literal["completed", "running"] ] = None
    created: Optional[datetime] 
    
class TaskResponse(CreateTask):
    id:int     #Define by System. Autoincrement Id

    