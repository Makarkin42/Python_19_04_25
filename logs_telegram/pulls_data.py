from sqlalchemy import create_engine, Column, Integer, String, PickleType
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///data_tg_pulls.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Questions(Base):
    __tablename__ = "Questions"
    id = Column(Integer, primary_key=True)
    list = Column(PickleType)
    title = Column(String)

class Answers(Base):
    __tablename__ = "Answers"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    que_id = Column(Integer)
    answers = Column(PickleType)

Base.metadata.create_all(engine)