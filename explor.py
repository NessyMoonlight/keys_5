import main as main
from tkinter import *
from tkinter import messagebox
import ru_local as ru



def event1():
    print(ru.EVENT_1)
    print(ru.EVENT_1_1)
    print(ru.EVENT_1_2)
    root = Tk()
    root.title(ru.EVENT_1)
    root.geometry("100x100")

    frame_top = Frame(root)
    frame_top.pack(side=TOP)

    frame_bottom1 = Frame(root, bg="white")
    frame_bottom1.pack(side=BOTTOM)

    def end1():
        if main.Room.map > 0:
            main.Room.map -= 1
        main.Room.axe += 1
        main.Room.food += 4
        messagebox.showinfo(message=ru.EVENT_1_YES)
        root.destroy()

    def end2():
        if main.Room.map > 0:
            main.Room.map -= 1
        if main.Room.water > 4:
            main.Room.water -= 4
        elif main.Room.water > 0:
            main.Room.water = 0
        if main.Room.food > 0:
            main.Room.food -= 4
        messagebox.showinfo(message=ru.EVENT_1_NO)
        root.destroy()

    btn1 = Button(frame_bottom1, text=ru.EVENT_1_1, bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text=ru.EVENT_1_2, bg="brown", command=end2)
    btn2.pack(side=LEFT)

    

def event1():
    print(ru.EVENT_2)
    print(ru.EVENT_2_1)
    print(ru.EVENT_2_2)
    print(ru.EVENT_2_3)
    print(ru.EVENT_2_4)
    print(ru.EVENT_2_5)
    print(ru.EVENT_2_6)
    root = Tk()
    root.title(ru.EVENT_2)
    root.geometry("100x100")

    frame_top = Frame(root)
    frame_top.pack(side=TOP)

    frame_bottom1 = Frame(root, bg="white")
    frame_bottom1.pack(side=BOTTOM)

    def end1():
        if main.Room.soap > 0:
            main.Room.soap -= 1
        messagebox.showinfo(message="Исход1")
        root.destroy()

    def end2():
        if main.Room.dihlofos>0:
            main.Room.dihlofos -= 1
        if main.HP > 2:
            main.HP -= 2
        elif main.HP > 0:
            main.HP
        messagebox.showinfo(message="Исход2")
        root.destroy()

    def end4():
        if main.Room.water>0:
            main.Room.water -=1
        messagebox.showinfo(message="Исход3")
        root.destroy()

    def end5():
        if main.Room.map > 0:
            main.Room.map -= 1
        main.Room.axe += 1
        main.Room.food +=4
        messagebox.showinfo(message="Исход4")
        root.destroy()

    def end6():
        if main.Room.map>0:
            main.Room.map -= 1
        if main.Room.water > 4:
            main.Room.water -= 4
        elif main.Room.water >0:
            main.Room.water = 0
        if main.Room.food > 4:
            main.Room.food -= 4
        elif main.Room.food >0:
            main.Room.food = 0
        messagebox.showinfo(message="Исход5")
        root.destroy()    

    btn1 = Button(frame_bottom1, text=ru.EVENT_2_1, bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text=ru.EVENT_2_2, bg="brown", command=end2)
    btn2.pack(side=LEFT)

    btn4 = Button(frame_bottom1, text=ru.EVENT_2_4, bg="brown", command=end4)
    btn4.pack(side=LEFT)

    btn5 = Button(frame_bottom1, text=ru.EVENT_2_5, bg="brown", command=end5)
    btn5.pack(side=LEFT)

    btn6 = Button(frame_bottom1, text=ru.EVENT_2_6, bg="brown", command=end6)
    btn6.pack(side=LEFT)

def event3():
    print("ru.EVENT_1")
    print("ru.EVENT_1_1")
    print("ru.EVENT_1_2")
    root = Tk()
    root.title("Событие")
    root.geometry("100x100")

    frame_top = Frame(root)
    frame_top.pack(side=TOP)

    frame_bottom1 = Frame(root, bg="white")
    frame_bottom1.pack(side=BOTTOM)

    def end1():
        messagebox.showinfo(message="Исход1")
        root.destroy()
    
    def end2():
        messagebox.showinfo(message="Исход2")
        root.destroy()

    def end3():
        messagebox.showinfo(message="Исход1")
        root.destroy()
    
    def end4():
        if main.HP > 0:
            main.HP -=1
        messagebox.showinfo(message="Исход2")
        root.destroy()    
    
    btn1 = Button(frame_bottom1, text="Выбор 1", bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text="Выбор 2", bg="brown", command=end2)
    btn2.pack(side=LEFT)

    btn3 = Button(frame_bottom1, text="Выбор 3", bg="brown", command=end3)
    btn3.pack(side=LEFT)

    btn4 = Button(frame_bottom1, text="Выбор 4", bg="brown", command=end4)
    btn4.pack(side=LEFT)

def btn_click():
    hp = Ted.hp
    inventory = Ted.inventory
    hunger = Ted.hunger
    thrust = Ted.thrust
    info = f"{str(hp)} ted's hp, {str(inventory)} ted's inventory, {str(hunger)} ted's, {str(thrust)} ted's"
    messagebox.showerror(title="ted", message=info)


def btn1_click():
    event2()


root = Tk()
root.title("Игра")
root.geometry("300x250")


frame = Frame(root, bg="black")
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

btn = Button(frame, text="карточка Теда", bg="red", command=main.day_start)
btn.pack()

btn1 = Button(frame, text="-hp", bg="red", command=btn1_click)
btn1.pack()

root.mainloop()