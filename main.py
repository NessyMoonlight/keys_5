from tkinter import *
from tkinter import messagebox
import nachalo as nach
import random
import ru_local as ru


class chel():
    def __init__(self, idpers):
        self.idpers = idpers
        self.inventory = 0
        self.thrust = 4
        self.hunger = 4
        self.hp = 3
        self.max_hp = 3


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
        self.ammo = 0
        self.radio = 0
        self.rifel = 0

Ted = chel(1)

Dolores = chel(2)

Timmi = chel(3)

Mary = chel(4)

Room = room()


def exploror():
    i = random.randint(1, 10)
    if i == 1:
        explor_result(8, 0, 0, 0)
    elif i == 2:
        explor_result(0, 8, 0, 0)
    elif i == 3:
        explor_result(4, 0, 1, 0)
    elif i == 4:
        explor_result(0, 4, 0, 0)
    elif i == 5:
        explor_result(8, 8, 0, 0)
    elif i == 6:
        explor_result(4, 4, 0, 0)
    elif i == 7:
        explor_result(0, 0, 0, 0)
    elif i == 8:
        explor_result(2, 2, 0, 1)
    elif i == 9:
        explor_result(0, 0, 1, 0)
    else:
        explor_result(0, 0, 1, 0)


def explor_result(food, water, medkit, cat):
    Room.food += food
    Room.water += water
    Room.medkit += medkit
    Room.cat += cat

def day_start():
    root = Tk()
    root.title("Раздача ресурсов")
    root.geometry("300x250")

    if Ted:
        Ted.hunger -= 1
        Ted.thrust -=1
    if Dolores:
        Dolores.hunger -=1
        Dolores.thrust -=1
    if Timmi:
        Timmi.hunger -=1
        Timmi.thrust -=1
    if Mary:
        Mary.hunger -=1
        Mary.thrust -=1

    def feed_ted():
        if Room.food>0:
            Ted.hunger += 1
            Room.food -=1
        else:
            print("Еды нет")
    def feed_dolores():
        if Room.food>0:
            Dolores.hunger += 1
            Room.food -=1
        else:
            print("Еды нет")
    def feed_timmi():
        if Room.food>0:
            Timmi.hunger += 1
            Room.food -=1
        else:
            print("Еды нет")
    def feed_mary():
        if Room.food>0:
            Mary.hunger += 1
            Room.food -=1
        else:
            print("Еды нет")

    def drink_ted():
        if Room.water>0:
            Ted.thrust += 1  
            Room.water -= 1
        else:
            print("Воды нет") 
    def drink_dolores():
        if Room.water>0:
            Dolores.thrust += 1 
            Room.water -= 1
        else:
            print("Воды нет") 
    def drink_timmi():
        if Room.water>0:
            Timmi.thrust += 1 
            Room.water -= 1
        else:
            print("Воды нет") 
    def drink_mary():
        if Room.water>0:
            Mary.thrust += 1   
            Room.water -= 1
        else:
            print("Воды нет")                     

    frame = Frame(root)
    frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    if Ted:
        btn = Button(frame, text="Кормить Теда", bg="red", command=feed_ted)
        btn.pack()
    if Ted:
        btn1 = Button(frame, text="Поить Теда", bg="red", command=drink_ted)
        btn1.pack()

    if Dolores:
        btn3 = Button(frame, text="Кормить Долорес", bg="red", command=feed_dolores)
        btn3.pack()
    if Dolores:
        btn4 = Button(frame, text="Поить Долорес", bg="red", command=drink_dolores)
        btn4.pack()

    if Timmi:
        btn5 = Button(frame, text="Кормить Тимми", bg="red", command=feed_timmi)
        btn5.pack()
    if Timmi:
        btn6 = Button(frame, text="Поить Тимми", bg="red", command=drink_timmi)
        btn6.pack()

    if Mary:
        btn7 = Button(frame, text="Кормить Мари", bg="red", command=feed_mary)
        btn7.pack()
    if Mary:
        btn8 = Button(frame, text="Поить Мари", bg="red", command=drink_mary)
        btn8.pack()

    btn2 = Button(frame, text="Выход", bg="red", command=root.destroy)
    btn2.pack(side=BOTTOM)

    root.mainloop()

def day1():
    print("Текст день 1")
    if Ted.hunger == 0 or Ted.thrust == 0 or Ted.hp == 0:
        Ted.__del__()
        print("Tед мертв")
    if Dolores.hunger == 0 or Dolores.thrust == 0 or Dolores.hp == 0:
        Dolores.__del__()
        print("Доллорес мертва")
    if Timmi.hunger == 0 or Timmi.thrust == 0 or Timmi.hp == 0:
        Timmi.__del__()
        print("Тимми мерт")
    if Mary.hunger == 0 or Mary.thrust == 0 or Mary.hp == 0:
        Mary.__del__()
        print("Мари мертва") 
    day_start()   

