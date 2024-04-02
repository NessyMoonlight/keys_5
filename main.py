from tkinter import *
from tkinter import messagebox
class ted():
   def __init__ (self, inventory, thrust, hunger, hp, max_inventory, max_thrust, max_hunger, max_hp):
       self.inventory = inventory
       self.thrust = thrust
       self.hunger = hunger
       self.hp = hp
       self.max_inventory = 0
       self.max_thrust = 4
       self.max_hunger = 4
       self.max_hp = 3

t=ted(0,4,4,3,0,0,0,0)

root = Tk()
def btn_click():
    hp = t.hp
    inventory = t.inventory
    hunger = t.hunger
    thrust = t.thrust
    info = f"{str(hp)} ted's hp, {str(inventory)} ted's inventory, {str(hunger)} ted's, {str(thrust)} ted's"
    messagebox.showinfo(title="ted", message=info)
def btn1_click():
    if t.hp > 0:
        t.hp -= 1


root.title("Игра")
root.geometry("300x250")

canvas = Canvas(root, width=300, height=250)
canvas.pack()

frame = Frame(root, bg="white")
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

btn = Button(frame, text="карточка Теда", bg="red", command=btn_click)
btn.pack()

btn1 = Button(frame, text="карточка Теда", bg="red", command=btn1_click)
btn1.pack()


root.mainloop()
