from sqlalchemy import create_engine, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime, date

engine = create_engine("sqlite:///generators_db.db")

class Base(DeclarativeBase):
  pass


class User(Base):
  __tablename__ = "users"

  id: Mapped[int] = mapped_column(primary_key=True)
  username: Mapped[str] = mapped_column(String(50))
  password: Mapped[str] = mapped_column(String(50))



class UserRequests(Base):
  __tablename__ = "user_requests"

  id: Mapped[int] = mapped_column(primary_key=True)
  username: Mapped[str] = mapped_column(String(50))
  gen_request: Mapped[str] = mapped_column(String())
  gen_response: Mapped[str] = mapped_column(String())
  date: Mapped[str] = mapped_column(default=str(date.today()))
  time: Mapped[str] = mapped_column(default=str(datetime.now().strftime('%H:%M:%S')))


class AuthLogs(Base):
  __tablename__ = "auth_logs"
  
  id: Mapped[int] = mapped_column(primary_key=True)
  date: Mapped[str] = mapped_column(default=str(date.today()))
  time: Mapped[str] = mapped_column(default=str(datetime.now().strftime('%H:%M:%S')))
  authorised: Mapped[bool] = mapped_column(Boolean())


class Client(Base):
  __tablename__ = "client"

  client_id: Mapped[str] = mapped_column(String(), primary_key=True)
  client_secret: Mapped[str] = mapped_column(String(), unique=True, index=True, nullable=False)
  user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
  redirect_uri: Mapped[str] = mapped_column(String())
  scope: Mapped[str] = mapped_column(String())


class Grant(Base):
  __tablename__ = "grant"

  id: Mapped[int] = mapped_column(primary_key=True)
  client_id: Mapped[str] = mapped_column(ForeignKey("client.client_id"))
  code: Mapped[str] = mapped_column(String())
  user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
  redirect_uri: Mapped[str] = mapped_column(String())
  expires: Mapped[datetime] = mapped_column(DateTime())
  scope: Mapped[str] = mapped_column(String())


class Token(Base):
  __tablename__ = "token"

  id: Mapped[int] = mapped_column(primary_key=True)
  client_id: Mapped[int] = mapped_column(ForeignKey("client.client_id"))
  user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
  token_type: Mapped[str] = mapped_column(String())
  access_token: Mapped[str] = mapped_column(String(255), unique=True)
  refresh_token: Mapped[str] = mapped_column(String(255), unique=True)
  expires: Mapped[datetime] = mapped_column(DateTime())
  scope: Mapped[str] = mapped_column(String())


Base.metadata.create_all(engine)