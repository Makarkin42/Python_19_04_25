from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:4252@localhost:5432/postgres")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Engine(Base):
    __tablename__ = "Energetika"
    id = Column(Integer, primary_key=True)
    naselenie = Column(Integer, nullable=False)
    power = Column(Integer, nullable=False)
    degree = Column(Integer, nullable=False)
    night = Column(Integer, nullable=False)

Base.metadata.create_all(engine)