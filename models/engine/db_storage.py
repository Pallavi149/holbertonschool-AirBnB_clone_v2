#!/usr/bin/python3
"""This module defines a class to manage DBstorage"""
import MySQLdb
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


ModelDict = {
    'User': User,
    'Place': Place,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Review': Review
}


class DBStorage:
    """This class manages storage of hbnb models"""
    __engine = "None"
    __session = "None"

    def __init__(self):

        # Retrieve the value of the "HBNB_MYSQL_USER" environment variable
        user = os.environ.get("HBNB_MYSQL_USER")
        password = os.environ.get("HBNB_MYSQL_PWD")
        # Retrieve the value of the "HBNB_MYSQL_HOST" environment variable with
        # a default value
        host = os.environ.get("HBNB_MYSQL_HOST", "localhost")
        database = os.environ.get("HBNB_MYSQL_DB")

        db_url = (f"mysql+mysqldb://{user}:{password}@{host}/{database}")
        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            print("test env: dropping all table")
            Base.metadata.drop_all(bind=self.__engine)

        # scoped_session to ensure thread_safety when creates a new database
        # session
        self.__session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))

    def all(self, cls=None):
        dictionary = {}
        if cls:
            modelClass = ModelDict[cls]
            self.readAllAsDict(cls, modelClass, dictionary)
        else:
            for className, modelClass in ModelDict.items():
                self.readAllAsDict(className, modelClass, dictionary)
        return dictionary

    def readAllAsDict(self, cls, modelClass, dictionary):
        if modelClass:
            records = self.__session.query(modelClass).all()
            for row in records:
                dictionary["{}.{}".format(cls, row.id)] = row

    def new(self, obj):
        """Adds object to current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits changes made to current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes a specified object from the current database section"""
        if obj:
            self.__session.delete()
        else:
            self.__session.query(self.__class__).delete()
        self.__session.commit()

    def reload(self):
        """Reloads data from the database"""
        if self.__session:
            self.__session.close()
        # Ensure all tables are created in the database
        Base.metadata.create_all(self.__engine)
        # scoped_session to ensure thread_safety when creates a new database
        # session
        self.__session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False))
