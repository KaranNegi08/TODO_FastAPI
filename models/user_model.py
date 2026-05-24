from  models.todo_model import Base
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, DateTime
from db import engine
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    username:Mapped[str] = mapped_column(String, nullable=False, unique=True)
    email:Mapped[str]= mapped_column(String, unique=True, nullable=False)
    hashed_password:Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self):
        return f"<Task username= {self.username} , email= {self.email}"


