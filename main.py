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

Room = room()

Ted = chel()

Dolores = chel() # объект класса

Timmi = chel()

Mary = chel() # объект класса



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


root = Tk()
def btn_click():
    hp = Ted.hp
    inventory = Ted.inventory
    hunger = Ted.hunger
    thrust = Ted.thrust
    info = f"{str(hp)} ted's hp, {str(inventory)} ted's inventory, {str(hunger)} ted's, {str(thrust)} ted's"
    messagebox.showerror(title="ted", message=info)
def btn1_click():
    if Ted.hp > 0:
        Ted.hp -= 1


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

авпвапвапвапва