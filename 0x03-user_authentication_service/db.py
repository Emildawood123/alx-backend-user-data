#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base
from user import User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """add_user for add user in db method"""
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        self.rollback()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """find_user_by method"""
        lst = ["id", 'email', 'hashed_password', 'session_id', 'reset_token']
        for k, v in kwargs.items():
            if k not in lst:
                raise InvalidRequestError()
        find_user = self._session.query(User).filter_by(**kwargs).first()
        if find_user:
            return find_user
        else:
            raise NoResultFound()

    def update_user(self, user_id, **kwargs) -> None:
        """update_user method"""
        lst = ["id", 'email', 'hashed_password', 'session_id', 'reset_token']
        for k, v in kwargs.items():
            if k not in lst:
                raise ValueError
        user_selected = self.find_user_by(id=user_id)
        for k, v in kwargs.items():
            setattr(user_selected, k, v)
        self._session.commit()
