from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///data_intexer.db")
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
        return False, False, False


class Tights(Base):
    __tablename__ = "tights"
    gender = Column(String, primary_key=True)
    size = Column(String, primary_key=True)  # Размер (S, M, L, XL)
    min_ankle = Column(Integer)
    max_ankle = Column(Integer)
    min_shin = Column(Integer)
    max_shin = Column(Integer)
    min_okrb = Column(Integer)    #Окружность бедер
    max_okrb = Column(Integer)
    min_obhvb = Column(Integer)       #Обхват бедер
    max_obhvb = Column(Integer)
    min_obhvt = Column(Integer)       #Обхват талии
    max_obhvt = Column(Integer)
    min_feet = Column(Integer)
    max_feet = Column(Integer)


    @classmethod
    def getting_size(cls,
                 gender: str,
                 ankle_size: int,
                 shin_size: int,
                 okr_b_size: int,
                 obhv_b_size: int,
                 obhvt_size: int,
                 feet_size: int):
        """Метод для получения размера продукта по параметрам"""
        anklee = session.query(cls).filter(cls.gender == gender, cls.min_ankle <= ankle_size, cls.max_ankle > ankle_size).all()
        shinn = session.query(cls).filter(cls.gender == gender, cls.min_shin <= shin_size, cls.max_shin > shin_size).all()
        feett = session.query(cls).filter(cls.gender == gender, cls.min_feet <= feet_size, cls.max_feet > feet_size).all()
        okr_b = session.query(cls).filter(cls.gender == gender, cls.min_okrb <= okr_b_size, cls.max_okrb > okr_b_size).all()
        obhv_b = session.query(cls).filter(cls.gender == gender, cls.min_obhvb <= obhv_b_size, cls.max_obhvb > obhv_b_size).all()
        obhv_t = session.query(cls).filter(cls.gender == gender, cls.min_obhvt <= obhvt_size, cls.max_obhvt > obhvt_size).all()

        if anklee and shinn and feett and okr_b and obhv_b and obhv_t:
            return anklee[0].size, shinn[0].size, feett[0].size, okr_b[0].size, obhv_b[0].size, obhv_t[0].size
        return False, False, False, False, False, False


class Chulki_pregnant(Base):
    __tablename__ = "chulki4pregnant2"
    gender = Column(String, primary_key=True)
    size = Column(String, primary_key=True)  # Размер (S, M, L, XL)
    num = Column(Integer)
    min_ankle = Column(Integer)
    max_ankle = Column(Integer)
    min_shin = Column(Integer)
    max_shin = Column(Integer)
    min_okrb = Column(Integer)
    max_okrb = Column(Integer)
    min_wide = Column(Integer)
    max_wide = Column(Integer)
    min_feet = Column(Integer)
    max_feet = Column(Integer)
    min_lenght = Column(Integer)
    max_lenght = Column(Integer)

    @classmethod
    def getting_size(cls,
                     gender: str,
                     ankle_size: int,
                     shin_size: int,
                     okr_b_size: int,
                     wide_size: int,
                     rost_size: int,
                     feet_size: int):
        anklee = session.query(cls).filter(cls.gender == gender, cls.min_ankle <= ankle_size,
                                           cls.max_ankle > ankle_size).all()
        shinn = session.query(cls).filter(cls.gender == gender, cls.min_shin <= shin_size,
                                          cls.max_shin > shin_size).all()
        feett = session.query(cls).filter(cls.gender == gender, cls.min_feet <= feet_size,
                                          cls.max_feet > feet_size).all()
        okr_b = session.query(cls).filter(cls.gender == gender, cls.min_okrb <= okr_b_size,
                                          cls.max_okrb > okr_b_size).all()
        wide = session.query(cls).filter(cls.gender == gender, cls.min_wide <= wide_size,
                                           cls.max_wide > wide_size).all()
        rost = session.query(cls).filter(cls.gender == gender, cls.min_lenght <= rost_size,
                                         cls.max_lenght > rost_size).all()


        if wide:
            if not okr_b or int(wide[0].num) >= int(okr_b[0].num) or int(wide[0].num) == int(shinn[0].num):
                if anklee and shinn and feett and wide and rost:
                    print("ZHIR")
                    return anklee[0].size, shinn[0].size, feett[0].size, wide[0].size, "подходит", True
                return False, False, False, False, False, False
            else:
                if anklee and shinn and feett and okr_b and rost:
                    print("DRISHZH")
                    return anklee[0].size, shinn[0].size, feett[0].size, okr_b[0].size, "подходит", False
                return False, False, False, False, False, False
        else:
            if anklee and shinn and feett and okr_b and rost:
                print("IMBA!!!!!")
                return anklee[0].size, shinn[0].size, feett[0].size, okr_b[0].size, "подходит", False
            return False, False, False, False, False, False



class Chulki_def(Base):
    __tablename__ = "chulki_default"
    gender = Column(String, primary_key=True)
    size = Column(String, primary_key=True)  # Размер (S, M, L, XL)
    num = Column(Integer)
    min_ankle = Column(Integer)
    max_ankle = Column(Integer)
    min_shin = Column(Integer)
    max_shin = Column(Integer)
    min_okrb = Column(Integer)
    max_okrb = Column(Integer)
    min_wide = Column(Integer)
    max_wide = Column(Integer)
    min_feet = Column(Integer)
    max_feet = Column(Integer)

    @classmethod
    def getting_size(cls,
                     gender: str,
                     ankle_size: int,
                     shin_size: int,
                     okr_b_size: int,
                     wide_size: int,
                     feet_size: int):
        anklee = session.query(cls).filter(cls.gender == gender, cls.min_ankle <= ankle_size,
                                           cls.max_ankle > ankle_size).all()
        shinn = session.query(cls).filter(cls.gender == gender, cls.min_shin <= shin_size,
                                          cls.max_shin > shin_size).all()
        feett = session.query(cls).filter(cls.gender == gender, cls.min_feet <= feet_size,
                                          cls.max_feet > feet_size).all()
        okr_b = session.query(cls).filter(cls.gender == gender, cls.min_okrb <= okr_b_size,
                                          cls.max_okrb > okr_b_size).all()
        wide = session.query(cls).filter(cls.gender == gender, cls.min_wide <= wide_size,
                                           cls.max_wide > wide_size).all()


        if wide:
            if not okr_b or int(wide[0].num) >= int(okr_b[0].num) or int(wide[0].num) == int(shinn[0].num):
                if anklee and shinn and feett and wide:
                    print("ZHIR")
                    return anklee[0].size, shinn[0].size, feett[0].size, wide[0].size, True
                return False, False, False, False, False
            else:
                if anklee and shinn and feett and okr_b:
                    print("DRISHZH")
                    return anklee[0].size, shinn[0].size, feett[0].size, okr_b[0].size, False
                return False, False, False, False, False
        else:
            if anklee and shinn and feett and okr_b:
                print("IMBA!!!!!")
                return anklee[0].size, shinn[0].size, feett[0].size, okr_b[0].size, False
            return False, False, False, False, False

Base.metadata.create_all(engine)


# Здесь можно протестировтаь работу методов и функций
if __name__ == "__main__":
    pass
    #Stockings.add_product()
    print(Chulki_pregnant.getting_size("male",  ankle_size=32, shin_size=40, feet_size=40, okr_b_size=70, wide_size=70, rost_size=80))
