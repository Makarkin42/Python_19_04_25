import random
import time
class Hero:
    def __init__(self,health = 100, damage = 15, name = "unit",wins = 0):
        self.health = health
        self.damage = damage
        self.name = name
        self.wins = wins
        self.XP = 0
        self.level = 1
    def klich(self):
        print("Я иду за вами!!!")
    def heal(self):
        luck = random.random()
        if luck <= 0.7:
            lucky = random.randint(10,99)
            self.health += lucky
            print(f"Ты нашел зелье лечения! Теперь у тебя {self.health} здоровья!")
            print('   ')
            time.sleep(1)
    def up(self):
        if self.XP >= 3:
            self.health = int(self.health * 1.2)
            self.damage = int(self.damage * 1.2)
            self.XP *= 0
            print(f"{self.name} прокачался! Теперь у меня {self.health} здоровья"
                  f" и {self.damage} урона!")
            print('   ')

    def attack(self,victim):
        victim.health -= self.damage
        print(f"Ты ударил врага, у него осталось {victim.health} здоровья")
        time.sleep(0.5)
        if victim.health <= 0:
            print(f"{victim.name} умер в этом бою!")
            return False
        return True

enemies = {"Огр": (220, 6), "Крыса": (60, 14), "Титан": (250, 6),
           "Мутант": (110, 10), "Киборг": (140, 12)}

bosses = {"Часовой": (320, 20), "Генерал": (400, 30), "Великий": (650, 28),
           "Выживший": (800, 50)}

class Enemy:
    def __init__(self):
        self.name = random.choice(tuple(enemies))
        self.health = int(enemies[self.name][0] * hero.level)
        self.damage = int(enemies[self.name][1] * hero.level)
        self.XP = 1
    def attack(self,victim):
        victim.health -= self.damage
        print(f"Враг тебя ударил! У тебя осталось {victim.health} здоровья")
        time.sleep(0.5)
        if victim.health <= 0:
            print(f"{victim.name} умер в этом бою!")
            return False
        return True

class Boss:
    def __init__(self):
        self.name = tuple(bosses)[hero.wins//6]
        self.health = bosses[self.name][0]
        self.damage = bosses[self.name][1]
        self.XP = 3
    def attack(self, victim):
        victim.health -= self.damage
        print(f"Босс тебя ударил! У тебя осталось {victim.health} здоровья")
        time.sleep(0.5)
        if victim.health <= 0:
            print(f"{victim.name} умер в этом бою!")
            return False
        return True

def start():
    print('Здравствуй путник! Не видел тебя раньше здесь\n')
    name_ans = input("Кем ты будешь у нас?\n")
    races = {
        "Дух": (210, 23),
        "Паладин": (350, 20),
        "Человек": (275, 22)}
    rase_ans = input(f"К какой расе ты относишься? {tuple (races)}\n").capitalize().strip()
    while rase_ans not in races:
        rase_ans = input(f"Выбери одну из этих рас: {tuple(races)}\n").capitalize().strip()

    profs = {
        "Маг": (0.8, 1.5),
        "Щитоносец": (1.7, 1),
        "Воин": (1.25, 1.25)}
    profs_ans = input(f"Кто ты по профессии? {tuple(profs)}\n").capitalize().strip()
    while profs_ans not in profs:
        profs_ans = input(f"Выбери одну из этих профессий: {tuple(profs)}\n").capitalize().strip()

    health = int(races[rase_ans][0] * profs[profs_ans][0])
    damage = int(races[rase_ans][1] * profs[profs_ans][1])
    time.sleep(1)
    print(f"У меня {health} здоровья и {damage} урона!")
    yes_ans = input("Ты готов отправиться в приключение?\n").capitalize().strip()
    while yes_ans not in ["Да","Нет"]:
        yes_ans = input(f"Ответь чётко: да или нет").capitalize().strip()
    if yes_ans == "Да":
        print('   ')
        return Hero(health=health,damage=damage,name=name_ans)
    else:
        print("Думаю ты ответил неправильно, создай персонажа ещё раз")
        return start()

def start_fight():
    if hero.wins%5 == 0 and hero.wins != 0:
        enemy = Boss()
    else:
        enemy = Enemy()
    print(f"На тебя напал(а) {enemy.name}! У него {enemy.health} здоровья и {enemy.damage} "
          "урона!")
    time.sleep(0.5)
    battle_ans = input("Начать бой (Да),или убежать (Нет)?\n").capitalize().strip()
    while battle_ans not in ["Да", "Нет"]:
        battle_ans = input("Ответь чётко: Да или Нет!\n").capitalize().strip()
    if battle_ans == "Да":
        print("Начался бой!")
        fight(enemy)
    elif battle_ans == "Нет":
        luck = random.random()
        if luck < 0.5:
            time.sleep(0.5)
            print("Ты смог убежать!")
            start_fight()
        else:
            time.sleep(1)
            print("Побег не удался! Враг стал сильнее! Бой начинается")
            enemy.damage =int(enemy.damage * 1.2)
            fight(enemy)



def fight(enemy):
    fight_res = hero.attack(enemy)
    if fight_res:
        fight_res = enemy.attack(hero)
        if fight_res:
            fight(enemy)
    else:
        print("Ты победил врага!")
        print('   ')
        hero.wins += 1
        hero.XP += enemy.XP
        hero.heal()
        hero.up()
        time.sleep(1)
        if (hero.wins - 1)%5 == 0 and (hero.wins - 1) != 0:
            hero.level += 0.35
        if hero.wins == 21:
            print("Ты спас эту зараженную планету от всех мутировавших боссов и врагов "
                  "которые здесь были. Твоя миссия выполнена!")
        else:
            start_fight()
hero = start()
start_fight()