import main as main
from tkinter import *
from tkinter import messagebox
import ru_local as ru

def event1():
    print(ru.EVENT_1)
    print(ru.EVENT_1_1)
    print(ru.EVENT_1_2)
    root = Tk()
    root.title("Событие")
    root.geometry("100x100")

    frame_top = Frame(root)
    frame_top.pack(side=TOP)

    frame_bottom1 = Frame(root, bg="white")
    frame_bottom1.pack(side=BOTTOM)

    def end1():
        main.Room.map -= 1
        main.Room.axe += 1
        main.Room.food +=4
        root.destroy()
    
    def end2():
        main.Room.map -= 1
        main.Room.water -= 4
        main.Room.food -=4
        root.destroy()
    
    btn1 = Button(frame_bottom1, text="Выбор 1", bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text="Выбор 2", bg="brown", command=end2)
    btn2.pack(side=LEFT)

    root.mainloop()


def event1():
    print("Условия")
    print("Выбор 1")
    print("Выбор 2")
    root = Tk()
    root.title("Событие")
    root.geometry("100x100")

    frame_top = Frame(root)
    frame_top.pack(side=TOP)

    frame_bottom1 = Frame(root, bg="white")
    frame_bottom1.pack(side=BOTTOM)

    def end1():
        main.Room.map -= 1
        main.Room.axe += 1
        main.Room.food +=4
        root.destroy()
    
    def end2():
        main.Room.map -= 1
        main.Room.water -= 4
        main.Room.food -=4
        root.destroy()
    
    btn1 = Button(frame_bottom1, text="Выбор 1", bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text="Выбор 2", bg="brown", command=end2)
    btn2.pack(side=LEFT)

    root.mainloop()