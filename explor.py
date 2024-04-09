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
        if main.Room.map >0:
            main.Room.map -= 1       
        main.Room.axe += 1
        main.Room.food +=4
        messagebox.showinfo(message="Исход1")
        root.destroy()
    
    def end2():
        if main.Room.map >0:
            main.Room.map -= 1
        if main.Room.water>4:
            main.Room.water -= 4
        elif main.Room.water >0:
            main.Room.water = 0
        if main.Room.food >0:
            main.Room.food -=4
        messagebox.showinfo(message="Исход2")
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
    print("Выбор 3")
    print("Выбор 4")
    print("Выбор 5")
    print("Выбор 6")
    root = Tk()
    root.title("Событие")
    root.geometry("100x100")

    frame_top = Frame(root)
    frame_top.pack(side=TOP)

    frame_bottom1 = Frame(root, bg="white")
    frame_bottom1.pack(side=BOTTOM)

    def end1():
        main.Room.soap -= 1
        root.destroy()
    
    def end2():
        main.Room.dihlofos -= 1
        main.HP -= 2
        root.destroy()
    
    
    def end4():
        main.Room.water -=1
        root.destroy()

    def end5():
        main.Room.map -= 1
        main.Room.axe += 1
        main.Room.food +=4
        root.destroy()
    
    def end6():
        main.Room.map -= 1
        main.Room.water -= 4
        main.Room.food -=4
        root.destroy()    

    btn1 = Button(frame_bottom1, text="Выбор 1", bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text="Выбор 2", bg="brown", command=end2)
    btn2.pack(side=LEFT)


    btn4 = Button(frame_bottom1, text="Выбор 4", bg="brown", command=end4)
    btn4.pack(side=LEFT)

    btn5 = Button(frame_bottom1, text="Выбор 5", bg="brown", command=end5)
    btn5.pack(side=LEFT)

    btn6 = Button(frame_bottom1, text="Выбор 6", bg="brown", command=end6)
    btn6.pack(side=LEFT)

    root.mainloop()