import s_taper
from s_taper.consts import *
import random

scheme = {
    "user_id": TEXT+KEY,"Инвентарь": TEXT
}
users = s_taper.Taper("Инвентарь","data.db").create_table(scheme)

inv = {"Яблоко": "2", "Петарда": "🚓🚓🚙"}
users.write(["yoki",inv])
print(users.read_all())
luck = random.random()
print(luck)
