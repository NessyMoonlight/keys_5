import random
import main as m
import dop_local as ru

class room():
    def __init__(self):
        self.water = 0
        self.food = 0
        self.knife = 0
        self.medkit = 0
        self.cat = 0
        self.map = 1
        self.axe = 0
        self.soap = 0
        self.dihlofos = 0
        self.lock = 0
        self.book = 0
        self.rifle = 0
        self.lantern = 0


Room = room()

p_1 = input(ru.BEGINNING)
p_2 = input(ru.BEGINNING)
p_3 = input(ru.BEGINNING)
p_4 = input(ru.BEGINNING)
ps = [p_1, p_2, p_3, p_4]

print(text1) # из констант

def kitchen(food, water, medkit):
    answer = [int(input(random.choice(ps), ru.KITCHEN))]
    if '4' in answer:
        Room.food += 1
    elif '5' in answer:
        Room.water += 1
    elif '8' in answer:
        Room.water += 1
    elif '9' in answer:
        Room.medkit += 1
    elif '1' in answer:
        Room.knife += 1


def liv_r():
    answer = [int(input(random.choice(ps), ru.LIV_R))]
    if '1' in answer:
        Room.lock += 1
    elif '4' in answer:
        Room.book += 1
    elif '5' in answer:
        Room.food += 1
    elif '6' in answer:
        Room.axe += 1
    elif '7' in answer:
        Room.rifle += 1


def bath():
    answer = [int(input(random.choice(ps), ru.BATH))]
    if '1' in answer:
        Room.medkit += 1
    elif '2' in answer:
        Room.soap += 1
    elif '4' in answer:
        Room.water += 1
    elif '5' in answer:
        Room.dihlofos += 1
    elif '6' in answer:
        Room.water += 1


def child():
    answer = [int(input(random.choice(ps), ru.CHILD))]
    if '1' in answer:
        Room.lantern += 1
    elif '2' in answer:
        Room.food += 1
    elif '8' in answer:
        Room.book += 1
    elif '9' in answer:
        Room.water += 1

