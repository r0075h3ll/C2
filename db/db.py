# from settings import DB_NAME, DB_USER, DB_PASSWORD
import sys
import logging
from sanic import Sanic
# import psycopg2
from sqlalchemy import create_engine, Column, Integer, String, insert, ForeignKey, select
from sqlalchemy.orm import sessionmaker, declarative_base, mapped_column, relationship
# from sqlalchemy.ext.declarative import declarative_base

handler = logging.StreamHandler(sys.stdout)
logger = logging.getLogger()
logger.setLevel("INFO")
logger.addHandler(handler)

# logger.info("%s %s %s" % (DB_USER, DB_NAME, DB_PASSWORD))

# conn = psycopg2.connect(host="localhost", port=1337, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
# query = "select * from tasks;"

# cursor = conn.cursor()

# cursor.execute(query)

# print(cursor.fetchone())

DB_NAME = None
DB_USER = None
DB_PASSWORD = None

engine = create_engine('postgresql://postgres:admin@localhost:1337/seatwo')
Session = sessionmaker(bind=engine)
session = Session()

# logger.info(session)

Base = declarative_base()

class AgentModel(Base):
    __tablename__ = 'agents'
    
    id = Column(Integer, primary_key=True)
    uuid = Column(String, unique=True, nullable=False)
    # tasks = relationship("TaskModel", back_populates="agent")

class TaskModel(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True)
    task = Column(String, nullable=False)
    uuid = Column(String)
    
    # Establishing the relationship with the AgentModel
    # agent = relationship("AgentModel", back_populates="tasks")

class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)


# logger.info("Here")
# users = session.query(User).all()
# for user in users:
#   print(user.uuid, user.task)

if __name__ == "__main__":
    DB_NAME, DB_USER, DB_PASSWORD = Sanic.get_app("C2").config.secrets['DB_NAME'], Sanic.get_app("C2").config.secrets['DB_USER'], Sanic.get_app("C2").config.secrets['DB_PASSWORD']
