from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///data_intext.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

GENDER = ("male", "female")
SIZES = ("S", "M", "L", "XL")

'''
Для каждого товара можно создать отдельный класс со своими методами. 
Обычно такие классы создают в отдельных файлах, а потом их все импортируют 
в один главный файл.
'''

class Stockings(Base):
    """Класс для таблицы чулок (мужских и женских)"""
    __tablename__ = "stockings"
    gender = Column(String, primary_key=True)  # Пол
    size = Column(String, primary_key=True)  # Размер (S, M, L, XL)
    min_shin = Column(Integer)  # Голень
    max_shin = Column(Integer)
    min_feet = Column(Integer)  # Стопа
    max_feet = Column(Integer)
    min_ankle = Column(Integer)  # Лодыжка
    max_ankle = Column(Integer)

    @classmethod
    def add_product(cls):
        """Удобный метод для добавления товара с проверками правильности"""
        print("Для добавления нового продукта введите его данные ниже")
        data = {}

        gender = input("Введите пол: ").strip().lower()
        while gender not in GENDER:
            gender = input("Введите пол: ").strip()
        data['gender'] = gender

        size = input("\nВведите размер: ").strip().upper()
        while size not in SIZES:
            size = input("Введите размер: ").strip().upper()
        data['size'] = size

        for key, body_part in (('shin', "голени"),
                               ('feet', "стопы"),
                               ('ankle', "лодыжки")):
            minimum = input(f"\nВведите размер {body_part}\nМинимальный: ").strip()
            maximum = input("Максимальный: ").strip()
            while not (minimum.isdigit() and maximum.isdigit()) or int(minimum) > int(maximum):
                print("Неверные размеры, проверьте данные!")
                minimum = input(f"Введите размер {body_part}\nМинимальный: ").strip()
                maximum = input("Максимальный: ").strip()
            data[f"min_{key}"] = minimum
            data[f"max_{key}"] = maximum

        product = Stockings(**data)  # Все ключи словаря становятся атрибутами экземпляра
        session.merge(product)
        session.commit()

    '''
    С помощью метода ниже удобно реализовать подбор размера по параметрам ноги клиента.
    У нас сохранены макисмальные и минимальные значения для каждого размера. 
    Достаточно сравнить размеры клиента с размерами товара.
    
    Проблема будет если, например, голень размера S, а лодыжка размера L, 
    то какой размер рекомендовать? 
    Нужно уточнить какие рекомендации даются реальными продавцами.
    '''

    @classmethod
    def get_size(cls,
                 gender: str,
                 ankle_size: int,
                 shin_size: int,
                 feet_size: int):
        """Метод для получения размера продукта по параметрам"""
        anklee = session.query(cls).filter(cls.gender == gender, cls.min_ankle <= ankle_size, cls.max_ankle > ankle_size).all()
        shinn = session.query(cls).filter(cls.gender == gender, cls.min_shin <= shin_size, cls.max_shin > shin_size).all()
        feett = session.query(cls).filter(cls.gender == gender, cls.min_feet <= feet_size, cls.max_feet > feet_size).all()

        if shinn and feett and anklee:
            return anklee[0].size, shinn[0].size, feett[0].size
        return None


Base.metadata.create_all(engine)

# сам размер  обхват голени↓↓↓                длина стопы↓↓↓    обхват лодыжки↓↓↓
#    1(S)	29 30 31 32 33 34 35 36 37	        35 36 37 38	  19 20 21 22
#    2(M)	34 35 36 37 38 39 40 41 42	        37 38 39	  22 23 24 25
#    3(L)	38 39 40 41 42 43 44 45 46 47 48	38 39 40	  25 26 27 28
#    4(XL)	41 42 43 44 45 46 47 48 49 50 51	39 40 41	  29 30 31 32

# Здесь можно протестировтаь работу методов и функций
if __name__ == "__main__":
    # Добавить новый продукт
    #Stockings.add_product()

    # Вернет S, если он есть в таблице
    print(Stockings.get_size("male", shin_size=32, feet_size=36, ankle_size=20))
