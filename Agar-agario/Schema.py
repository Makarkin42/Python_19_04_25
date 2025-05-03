from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:4252@localhost:5432/postgres")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Stats(Base):
    __tablename__ = "agario"
    id = Column(Integer, primary_key=True)
    username = Column(String(36), nullable=False)
    x = Column(Integer)
    y = Column(Integer)
    xspeed = Column(Integer, default=0)
    yspeed = Column(Integer, default=0)
    abspeed = Column(Integer, default=1)
    color = Column(String, default="white")
    size = Column(Integer, default=35)
    adress = Column(String(40))

Base.metadata.create_all(engine)