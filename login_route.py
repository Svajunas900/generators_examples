from main import app
from flask import session
from sqlalchemy.orm import Session
from models import User, engine


@app.post("/login")
def login(username: str, password: str):
  session["username"] = username
  session["user_id"] = 1
  with Session(engine) as session:
    user = User(id=1, username=username, password=password)
    session.add(user)
    session.commit()