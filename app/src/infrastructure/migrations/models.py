import os

import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeMeta


class Base(DeclarativeMeta):
    pass


class User(Base):
    __tablename__ = "users"
    id: int = sa.Column(sa.Integer)
    username: str = sa.Column(sa.String(length=32))
    firstname: str =sa.Column(sa.String(length=100))
    lastname: str = sa.Column(sa.String(length=100)) 


class UserData(Base):
    __tablename__ = "users_data"
    data1: str = sa.Column(sa.String(length=2048))
    data2: int = sa.Column(sa.Integer)


class UserUserData(Base):
    __tablename__ = "relationships_user"
    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id', ondelete="CASCADE"))
    user_data_id = sa.Column(sa.Integer, sa.ForeignKey('users_data.id', ondelete="CASCADE"))