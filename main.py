from tkinter import *
from tkinter import messagebox
import nachalo as nach
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

Room = room()

Ted = chel()

Dolores = chel() # объект класса

Timmi = chel()

Mary = chel() # объект класса

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




блаблалалала