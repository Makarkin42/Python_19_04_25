from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import faker
import random

engine = create_engine("postgresql+psycopg2://postgres:4252@localhost:5432/postgres")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(36), nullable=False)
    password = Column(String(36), nullable=False)
    age = Column(Integer, default=-1)

class Heroes(Base):
    __tablename__ = "heroes"
    name = Column(String(16), primary_key=True)
    damage = Column(Integer, nullable=False)
    level = Column(Integer, default=1)
    health = Column(Integer, nullable=False)

Base.metadata.create_all(engine)

user = Users(username="master", password="98765", age=47)
fake = faker.Faker("ru_RU")
'''for i in range(200):
    agee = random.randint(4, 99)
    user = Users(username=fake.user_name(), password=fake.password(), age=agee)
    session.add(user)
session.commit()'''

'''for i in range(200):
    hero = Heroes(name=fake.middle_name(), damage=random.randint(10, 50), health=random.randint(50, 250),level=1)
    session.merge(hero)
session.commit()'''

alls = session.query(Heroes).all()
for user in alls:
    print(user.__dict__)

session.query(Heroes).filter(Heroes.health>=100, Heroes.damage>=20).update({"level": 2})
session.query(Heroes).filter(Heroes.health>=150, Heroes.damage>=30).update({"level": 3})
session.commit()

for i in range(1,4):
    olds = session.query(Heroes).filter(i==Heroes.level).all()
    print(len(olds), i)

session.query(Heroes).filter("Витальевич"==Heroes.name).delete()
session.commit()

one = session.get(Heroes, "Валерьянович")
print(one)

'''for i in olds:
    print(i.age, i.username)'''