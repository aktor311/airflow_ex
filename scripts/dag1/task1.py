import datetime as datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, VARCHAR, TIMESTAMP
class WeatherResult(Base):
    __tablename__ = 'Weather result'
    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    City = Column(VARCHAR(50), nullable=False)
    temperature = Column(VARCHAR(50), nullable=False)
    wind_speed = Column(VARCHAR(50), nullable=False)
    pressure = Column(VARCHAR(50), nullable=False)
    create_date = Column(TIMESTAMP, nullable=False, index=True)


SQLALCHEMY_DATABASE_URL = f"postgresql://admin:lw6er4t1@193.104.57.192:5432/homework" # Создает подключение к БД на сервере
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Base.metadata.create_all(bind = engine)   # СОЗДАЕМ ТАБЛИЦУ (BASE НАСЛЕДУЕТ WeatherResult из weather.py и на основе данного класса создает таблицу

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session_local = SessionLocal()

new_record = WeatherResult(
                    City='Tomsk',
                    temperature=0,
                    wind_speed=21,
                    pressure=10222,
                    create_date=datetime.datetime.utcnow()
                    )
new_record2 = WeatherResult(
                    City='Udomlya',
                    temperature=88,
                    wind_speed=6,
                    pressure=10200,
                    create_date=datetime.datetime.utcnow()
                    )

session_local.add(new_record)
session_local.add(new_record2)

session_local.commit()