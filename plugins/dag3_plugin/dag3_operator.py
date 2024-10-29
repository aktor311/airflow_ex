from airflow.models.baseoperator import BaseOperator
from airflow.models.connection import Connection
import datetime as datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, VARCHAR, Date, Boolean, Float, TIMESTAMP
from sqlalchemy.orm import declarative_base
Base = declarative_base()

class Currency(Base):
    __tablename__ = 'currency3'
    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    currency = Column(VARCHAR(50), nullable=False)
    value = Column(Float, nullable=False)
    currate_date = Column(TIMESTAMP, nullable=False, index=True, default=datetime.datetime.now)

class MyFirstExOperator(BaseOperator):
    def __init__(self,
                 postgre_conn: Connection,
                 currency: str,
                 value: float,
                 **kwargs) -> None:
        super().__init__(**kwargs)
        self.postgre_conn = postgre_conn
        self.currency = currency
        self.value = value
        self.SQLALCHEMY_DATABASE_URI = f"postgresql://{postgre_conn.login}:{postgre_conn.password}@{postgre_conn.host}:{str(postgre_conn.port)}/{postgre_conn.schema}"


    def execute(self, context):
        engine = create_engine(self.SQLALCHEMY_DATABASE_URI)
        Base.metadata.create_all(bind=engine)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        session_local = SessionLocal()

        new_record = Currency(
            currency=self.currency,
            value=self.value,
        )
        session_local.add(new_record)
        session_local.commit()