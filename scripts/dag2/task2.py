import datetime as datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, VARCHAR, Date, Boolean, Float, TIMESTAMP
from sqlalchemy.orm import declarative_base
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--date", dest="date")
parser.add_argument("--host", dest="host")
parser.add_argument("--dbname", dest="dbname")
parser.add_argument("--user", dest="user")
parser.add_argument("--jdbc_password", dest="jdbc_password")
parser.add_argument("--port", dest="port")
args = parser.parse_args()

print('date = ' + str(args.date))
print('host = ' + str(args.host))
print('dbname = ' + str(args.dbname))
print('user = ' + str(args.user))
print('jdbc_password = ' + str(args.jdbc_password))
print('port = ' + str(args.port))

v_host = str(args.host)
v_dbname = str(args.dbname)
v_user = str(args.user)
v_password = str(args.jdbc_password)
v_port = str(args.port)

Base = declarative_base()

class Humans(Base):
    __tablename__ = 'humans_from_dag2-task2'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    first_name = Column(VARCHAR(50), nullable=False)
    second_name = Column(VARCHAR(50), nullable=False)
    age = Column(Integer, nullable=False)
    current_date = Column(TIMESTAMP, nullable=False, index=True)

SQLALCHEMY_DATABASE_URI = f"postgresql://{str(v_user)}:{str(v_password)}@{str(v_host)}:{str(v_port)}/{str(v_dbname)}"

engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
session_local = SessionLocal()

new_record1 = Humans(
    first_name='Petya',
    second_name='Petrov',
    age=20,
    current_date=datetime.datetime.utcnow()
)

new_record2 = Humans(
    first_name='Vasya',
    second_name='Ivanov',
    age=22,
    current_date=datetime.datetime.utcnow()
)

new_record3 = Humans(
    first_name='Vanya',
    second_name='Popkin',
    age=28,
    current_date=datetime.datetime.utcnow()
)

session_local.add(new_record1)
session_local.add(new_record2)
session_local.add(new_record3)

session_local.commit()