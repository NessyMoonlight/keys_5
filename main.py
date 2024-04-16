# Case-study #5
# Developers: Borodin Artemiy, Solovyova Maria,
# Selikhova Polina, Lyamin Egor
#

from tkinter import *
from tkinter import messagebox
import nachalo as nach
import explor as ex
import random
import ru_local as ru


# creating a character class.
class chel():
    def __init__(self, name): # self is a characteristic of a class.
        self.name = name
        self.inventory = 0
        self.thirst = 6
        self.hunger = 6
        self.hp = 3
        self.max_hp = 3


# to delete a character.
    def __del__(self):
        print(f"{self.name} Умер")


# items from the inventory in the bunker.
class room():
    def __init__(self, water, food, knife, medkit, cat, map, axe, soap, dihlofos, lock, ammo, radio, rifel):
        self.water = water
        self.food = food
        self.knife = knife
        self.medkit = medkit
        self.cat = cat
        self.map = map
        self.axe = axe
        self.soap = soap
        self.dihlofos = dihlofos
        self.lock = lock
        self.ammo = ammo
        self.radio = radio
        self.rifel = rifel


Ted = chel("Ted")

Dolores = chel("Dolores")

Timmi = chel("Timmi")

Mary = chel("Mary")

# we transfer the things that we received at the unitial stage.
Room = room(nach.Rooom.water, nach.Rooom.food, nach.Rooom.knife, nach.Rooom.medkit, nach.Rooom.cat, nach.Rooom.map,
            nach.Rooom.axe, nach.Rooom.soap, nach.Rooom.dihlofos, nach.Rooom.lock, nach.Rooom.ammo, nach.Rooom.radio,
            nach.Rooom.rifle)


def live():
    """
    a function that checks if a character is alive
    and deletes it if dead
    """
    if Ted.hunger == 0 or Ted.thirst == 0 or Ted.hp == 0:
        Ted.__del__()
        print("Tед мертв")
    if Dolores.hunger == 0 or Dolores.thirst == 0 or Dolores.hp == 0:
        Dolores.__del__()
        print("Доллорес мертва")
    if Timmi.hunger == 0 or Timmi.thirst == 0 or Timmi.hp == 0:
        Timmi.__del__()
        print("Тимми мертв")
    if Mary.hunger == 0 or Mary.thirst == 0 or Mary.hp == 0:
        Mary.__del__()
        print("Мари мертва")
    if (Ted.hunger == 0 or Ted.thirst == 0 or Ted.hp == 0) and (
            Dolores.hunger == 0 or Dolores.thirst == 0 or Dolores.hp == 0) and (
            Timmi.hunger == 0 or Timmi.thirst == 0 or Timmi.hp == 0) and (
            Mary.hunger == 0 or Mary.thirst == 0 or Mary.hp == 0):
        exit()
    else:
        day_start()


def exploror():
    """
    the function of expeditions for a random character
    """
    d = random.randint(1, 4)
    if d == 1:
        print(ru.TED_EX)
    elif d == 2:
        print(ru.DOLORES_EX)
    elif d == 3:
        print(ru.MARY_EX)
    elif d == 4:
        print(ru.TIMMY_EX)
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
    """
    the result function of the expedition,
    which replenishes the inventory of the bunker
    """
    Room.food += food
    Room.water += water
    Room.medkit += medkit
    Room.cat += cat


def day_start():
    """
    a function that analyzes the parameters of the character
    and makes it possible to change them using available resources
    """
    if (Ted.hp and Dolores.hp and Timmi.hp and Mary.hp) <= 0:
        exit()
    else:
        root = Tk()
        root.title("Раздача ресурсов")
        root.geometry("300x250")

        frame = Frame(root)
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        if Ted:
            Ted.hunger -= 1
            Ted.thirst -= 1
            if Ted.hp > 0 and Ted.thirst > 0 and Ted.hunger > 0:
                print(f"Здоровье Теда{Ted.hp}\nЖажда Теда{Ted.thirst}\nГолод Теда{Ted.hunger}\n ================\n")

        if Dolores:
            Dolores.hunger -= 1
            Dolores.thirst -= 1
            if Dolores.hp > 0 and Dolores.thirst > 0 and Dolores.hunger > 0:
                print(
                    f"Здоровье Долорес{Dolores.hp}\nЖажда Долорес{Dolores.thirst}\nГолод Долорес{Dolores.hunger}\n ================\n")
        if Timmi:
            Timmi.hunger -= 1
            Timmi.thirst -= 1
            if Timmi.hp > 0 and Timmi.thirst > 0 and Timmi.hunger > 0:
                print(
                    f"Здоровье Тимми{Timmi.hp}\nЖажда Тимми{Timmi.thirst}\nГолод Тимми{Timmi.hunger}\n ================\n")
        if Mary:
            Mary.hunger -= 1
            Mary.thirst -= 1
            if Mary.hp > 0 and Mary.thirst > 0 and Mary.hunger > 0:
                print(f"Здоровье Мэри{Mary.hp}\nЖажда Мэри{Mary.thirst}\nГолод Мэри{Mary.hunger}\n ================\n")

        def feed_ted():
            if Room.food > 0:
                Ted.hunger += 1
                Room.food -= 1
            else:
                print("Еды нет")

        def feed_dolores():
            if Room.food > 0:
                Dolores.hunger += 1
                Room.food -= 1
            else:
                print("Еды нет")

        def feed_timmi():
            if Room.food > 0:
                Timmi.hunger += 1
                Room.food -= 1
            else:
                print("Еды нет")

        def feed_mary():
            if Room.food > 0:
                Mary.hunger += 1
                Room.food -= 1
            else:
                print("Еды нет")

        def drink_ted():
            if Room.water > 0:
                Ted.thirst += 1
                Room.water -= 1
            else:
                print("Воды нет")

        def drink_dolores():
            if Room.water > 0:
                Dolores.thirst += 1
                Room.water -= 1
            else:
                print("Воды нет")

        def drink_timmi():
            if Room.water > 0:
                Timmi.thirst += 1
                Room.water -= 1
            else:
                print("Воды нет")

        def drink_mary():
            if Room.water > 0:
                Mary.thirst += 1
                Room.water -= 1
            else:
                print("Воды нет")

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


def Main():
    nach

    ex.day1()


if __name__ == '__main__':
    Main()

