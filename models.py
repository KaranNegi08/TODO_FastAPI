from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Float, Integer, DateTime
from db import engine
from datetime import datetime
from db import Base

class Todo(Base):
    __tablename__ = "tasks"

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    task_name:Mapped[str] = mapped_column(String, nullable=False)
    task_description:Mapped[str]= mapped_column(String, nullable=False)
    status:Mapped[str] = mapped_column(String, nullable=False, default="running")
    created: Mapped[datetime]= mapped_column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Task id= {self.id} , name= {self.name}"


