import s_taper
from s_taper.consts import *
import faker
import random
import time

fake = faker.Faker("ru_RU")
scheme = {
    "user_id": TEXT+KEY,"nickname": TEXT, "age": INT, "first": BLN
}
users = s_taper.Taper("Users","data.db").create_table(scheme)
users.write(["makar888","Игрок",12,True])
# for i in range(300):
#      age = random.randint(5,85)
#      first = random.choice([True,False])
#      users.write([fake.user_name(),fake.first_name(),age,first])

ruriks = users.read("nickname",'Рюрик')
#print(ruriks)

data = users.read_all()
#print(data)

olds = 0
for i in data:
    if i[2] >= 50:
        olds += 1
        #print(i)
print(olds)

users.drop_table(table_name="user_pankrat06")

scheme = {"time": FLT}
for i in data:
    s_taper.Taper("user_"+i[0],"data.db").create_table(scheme)

users.delete_row("user_id","pankrat06")
pankrat = s_taper.Taper("user_pankrat06", "data.db").create_table(scheme)
pankrat.drop_table()

users.write([time.time()],table_name="user_gorde_38")

alls = users.read_all()
# for i in range(300):
#     user = random.choice(alls)
#     users.write([time.time()],table_name=f"user_{user[0]}")
#     print(user[0])

def mean(user_id):
    user = s_taper.Taper("user_" + user_id, "data.db").create_table(scheme)
    times = user.read_all()
    #print(times)
    mid = []
    enter = 0
    for i, sec in enumerate(times):
        sec = sec[0]
        #print(i,sec)
        if not i%2:
            enter = (sec)
        elif i%2:
            mid.append(int(sec - enter))
    print(sum(mid)/len(mid)/60)

mean("lev2009")