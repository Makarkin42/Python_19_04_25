import s_taper
from s_taper.consts import *
import faker
import random

fake = faker.Faker("ru_RU")
scheme = {
    "Имя": TEXT+KEY,"Здоровье": INT,"Урон": INT, "Уровень": INT, "Раса": TEXT
}
heroes = s_taper.Taper("heroes","data.db").create_table(scheme)

# for i in range(300):
#     Level = random.randint(1,99)
#     Race = random.choice(["Человек","Монстр","Робот"])
#     Hp = random.randint(1000,8000)
#     if Hp >= 4000:
#         Dmg = random.randint(80,150)
#     else:
#         Dmg = random.randint(120,250)
#     heroes.write([fake.first_name(),Hp,Dmg,Level,Race])

def middle(race):
    humans = heroes.read("Раса", race)
    humans_hp = 0
    for i in humans:
        humans_hp += i[1]
    humans_hp = int(humans_hp/ len(humans))
    humans_dmg = 0
    for i in humans:
        humans_dmg += i[2]
    humans_dmg = int(humans_dmg / len(humans))
    print(race, humans_hp,humans_dmg)

middle("Человек")
middle("Робот")
middle("Монстр")