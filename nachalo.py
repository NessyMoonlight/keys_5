import random
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
        self.ammo = 2
        self.radio = 1


Rooom = room()

p_1 = input(ru.BEGINNING)
p_2 = input(ru.BEGINNING)
p_3 = input(ru.BEGINNING)
p_4 = input(ru.BEGINNING)
ps = [p_1, p_2, p_3, p_4]
i = random.choice(ps)
food = 0
water = 0
medkit = 0

print("qsd") # из констант


answer = [input(f"{i} {ru.KITCHEN}")]
ps.remove(i)
if '4' in answer:
    Rooom.food += 2
    food +=1
elif '5' in answer:
    Rooom.water += 2
    water +=1
elif '8' in answer:
    Rooom.water += 2
    water +=1
elif '9' in answer:
    Rooom.medkit += 1
    medkit +=1
elif '1' in answer:
    Rooom.knife += 1
i = random.choice(ps)

answer = [input(f"{i} {ru.KITCHEN}")]
ps.remove(i)
if '1' in answer:
    Rooom.lock += 1
elif '4' in answer:
    Rooom.book += 1
elif '5' in answer:
    Rooom.food += 2
    food +=1
elif '6' in answer:
    Rooom.axe += 1
elif '7' in answer:
    Rooom.rifle += 1

i = random.choice(ps)


answer = [input(f"{i} {ru.KITCHEN}")]
ps.remove(i)
if '1' in answer:
    Rooom.medkit += 1
    medkit +=1
elif '2' in answer:
    Rooom.soap += 1
elif '4' in answer:
    Rooom.water += 2
    water +=1
elif '5' in answer:
    Rooom.dihlofos += 1
elif '6' in answer:
    Rooom.water += 2
    water +=1

i = random.choice(ps)

answer = [input(f"{i} {ru.KITCHEN}")]
ps.remove(i)
if '1' in answer:
    Rooom.lantern += 1
elif '2' in answer:
    Rooom.food += 2
    food +=1
elif '8' in answer:
    Rooom.book += 1
elif '9' in answer:
    Rooom.water += 2
    water +=1
      

if water == 0:
    Rooom.water += 8
if food == 0:
    Rooom.food +=8
if medkit== 0:
    Rooom.medkit +=1