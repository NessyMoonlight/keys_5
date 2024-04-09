from tkinter import *
from tkinter import messagebox
import nachalo as nach
import random
import ru_local as ru

class chel():
   def __init__(self,idpers):
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


Room = room()


def explor():
    i = random.randint(1,10)
    if i == 1:
        explor_result(8,0,0,0)
    elif i == 2:
        explor_result(0,8,0,0)
    elif i == 3:
        explor_result(4,0,1,0)
    elif i == 4:
        explor_result(0,4,0,0)
    elif i == 5:
        explor_result(8,8,0,0)
    elif i == 6:
        explor_result(4,4,0,0)
    elif i == 7:
        explor_result(0,0,0,0)
    elif i == 8:
        explor_result(2,2,0,1)
    elif i == 9:
        explor_result(0,0,1,0)
    else:
        explor_result(0,0,1,0)    

def explor_result(food,water,medkit,cat):
    Room.food += food
    Room.water += water
    Room.medkit += medkit
    Room.cat += cat

def event1():
    root = Tk()
    root.title("Событие")
    root.geometry("600x600")

    frame_top = Frame(root)
    frame_top.pack(side=TOP)

    frame_bottom1 = Frame(root, bg="white")
    frame_bottom1.pack(side=BOTTOM)

    laybel = Label(frame_top,text="Описание 1 события")
    laybel.pack(side=LEFT)

    laybel2 = Label(frame_top,text="Описание 2 события")
    laybel2.pack(side=LEFT)
    
    def end1():
        Room.map -= 1
        Room.axe += 1
        Room.food +=4
    
    btn1 = Button(frame_bottom1, text="Выбор 1", bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn1 = Button(frame_bottom1, text="Выбор 2", bg="brown", command=btn1_click)
    btn1.pack(side=LEFT)

    root.mainloop()


def btn_click():
    hp = Ted.hp
    inventory = Ted.inventory
    hunger = Ted.hunger
    thrust = Ted.thrust
    info = f"{str(hp)} ted's hp, {str(inventory)} ted's inventory, {str(hunger)} ted's, {str(thrust)} ted's"
    messagebox.showerror(title="ted", message=info)
def btn1_click():
    event1()

root = Tk()
root.title("Игра")
root.geometry("300x250")

#canvas = Canvas(root, width=300, height=250)
#canvas.pack()

frame = Frame(root, bg="black")
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

btn = Button(frame, text="карточка Теда", bg="red", command=btn_click)
btn.pack()

btn1 = Button(frame, text="-hp", bg="red", command=btn1_click)
btn1.pack()

root.mainloop()


    