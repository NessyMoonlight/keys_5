import main as main
from tkinter import *
from tkinter import messagebox
import ru_local as ru
import random


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

    

def event2():
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
        i = random.randint(1,4)
        if i ==1:
            if main.Ted.hp >2:
                main.Ted.hp -= 2
            else:
                main.Ted.hp == 0
        elif i ==2:
            if main.Timmi.hp >2:
                main.Timmi.hp -= 2
            else:
                main.Timmi.hp == 0
        elif i ==3:
            if main.Dolores.hp >2:
                main.Dolores.hp -= 2
            else:
                main.Dolores.hp == 0
        elif i ==4:
            if main.Mary.hp >2:
                main.Mary.hp -= 2
            else:
                main.Mary.hp == 0           
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
        i = random.randint(1,4)
        if i ==1:
            if main.Ted.hp >1:
                main.Ted.hp -= 1
            else:
                main.Ted.hp == 0
        elif i ==2:
            if main.Timmi.hp >1:
                main.Timmi.hp -= 1
            else:
                main.Timmi.hp == 0
        elif i ==3:
            if main.Dolores.hp >1:
                main.Dolores.hp -= 1
            else:
                main.Dolores.hp == 0
        elif i ==4:
            if main.Mary.hp >1:
                main.Mary.hp -= 1
            else:
                main.Mary.hp == 0
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

def event4():
    print("Условия")
    print("Выбор 1")
    print("Выбор 2")
    print("Выбор 3")
    print("Выбор 4")

    root = Tk()
    root.title("Событие")
    root.geometry("100x100")

    frame_top = Frame(root)
    frame_top.pack(side=TOP)

    frame_bottom1 = Frame(root, bg="white")
    frame_bottom1.pack(side=BOTTOM)

    def end1():
        if main.Room.rifle > 0:
            i = random.randint(1,4)
        if i ==1:
            if main.Ted.hp >1:
                main.Ted.hp -= 1
            else:
                main.Ted.hp == 0
        elif i ==2:
            if main.Timmi.hp >1:
                main.Timmi.hp -= 1
            else:
                main.Timmi.hp == 0
        elif i ==3:
            if main.Dolores.hp >1:
                main.Dolores.hp -= 1
            else:
                main.Dolores.hp == 0
        elif i ==4:
            if main.Mary.hp >1:
                main.Mary.hp -= 1
            else:
                main.Mary.hp == 0
            messagebox.showinfo(message="Исход1")
            root.destroy()

    def end2():
        messagebox.showinfo(message="Исход2")
        root.destroy()

    def end3():
        messagebox.showinfo(message="Исход3")
        root.destroy()

    def end4():
        messagebox.showinfo(message="Исход4")
        root.destroy()


    btn1 = Button(frame_bottom1, text="Выбор 1", bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text="Выбор 2", bg="brown", command=end2)
    btn2.pack(side=LEFT)

    btn3 = Button(frame_bottom1, text="Выбор 3", bg="brown", command=end3)
    btn3.pack(side=LEFT)

    btn4 = Button(frame_bottom1, text="Выбор 4", bg="brown", command=end4)
    btn4.pack(side=LEFT)


def event5():
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
        main.Room.food += 8
        messagebox.showinfo(message="Исход1")
        root.destroy()

    def end2():
        messagebox.showinfo(message="Исход2")
        root.destroy()


    btn1 = Button(frame_bottom1, text="Выбор 1", bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text="Выбор 2", bg="brown", command=end2)
    btn2.pack(side=LEFT)


def event6():
    print("Условия")
    print("Выбор 1")
    print("Выбор 2")
    print("Выбор 3")

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
        if main.Room.dihlofos > 0:
            main.Room.dihlofos -= 1
            messagebox.showinfo(message="Исход2")
            root.destroy()

    btn1 = Button(frame_bottom1, text="Выбор 1", bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text="Выбор 2", bg="brown", command=end2)
    btn2.pack(side=LEFT)

    btn3 = Button(frame_bottom1, text="Выбор 3", bg="brown", command=end3)
    btn3.pack(side=LEFT)


def event7():
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
        if main.Room.ammo > 0:
            main.Room.ammo -= 1
            main.Room.food += 8
            messagebox.showinfo(message="Исход1")
            root.destroy()

    def end2():
        messagebox.showinfo(message="Исход2")
        root.destroy()

    btn1 = Button(frame_bottom1, text="Выбор 1", bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text="Выбор 2", bg="brown", command=end2)
    btn2.pack(side=LEFT)


def event8():
    print("Условия")
    print("Выбор 1")
    print("Выбор 2")
    print("Выбор 3")

    root = Tk()
    root.title("Событие")
    root.geometry("100x100")

    frame_top = Frame(root)
    frame_top.pack(side=TOP)

    frame_bottom1 = Frame(root, bg="white")
    frame_bottom1.pack(side=BOTTOM)

    def end1():
        if main.Room.dihlofos > 0:
            main.Room.dihlofos -= 1
            main.Room.food += 2
            messagebox.showinfo(message="Исход1")
            root.destroy()

    def end2():
        if main.Room.rifle > 0:
            main.Room.food += 2
            messagebox.showinfo(message="Исход2")
            root.destroy()

    def end3():
        i = random.randint(1,4)
        if i ==1:
            if main.Ted.hp >2:
                main.Ted.hp -= 2
            else:
                main.Ted.hp == 0
        elif i ==2:
            if main.Timmi.hp >2:
                main.Timmi.hp -= 2
            else:
                main.Timmi.hp == 0
        elif i ==3:
            if main.Dolores.hp >2:
                main.Dolores.hp -= 2
            else:
                main.Dolores.hp == 0
        elif i ==4:
            if main.Mary.hp >2:
                main.Mary.hp -= 2
            else:
                main.Mary.hp == 0 
        messagebox.showinfo(message="Исход3")
        root.destroy()


    btn1 = Button(frame_bottom1, text="Выбор 1", bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text="Выбор 2", bg="brown", command=end2)
    btn2.pack(side=LEFT)

    btn3 = Button(frame_bottom1, text="Выбор 3", bg="brown", command=end3)
    btn3.pack(side=LEFT)


def event9():
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
        if main.Room.food > 2:
           main.Room.food -= 2
        elif main.Room.food > 0:
           main.Room.food = 0
           main.Room.medkit += 1
           main.Room.water += 2
        messagebox.showinfo(message="Исход1")
        root.destroy()

    def end2():
        messagebox.showinfo(message="Исход2")
        root.destroy()


    btn1 = Button(frame_bottom1, text="Выбор 1", bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text="Выбор 2", bg="brown", command=end2)
    btn2.pack(side=LEFT)


def event10():
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
        if main.Room.food > 2:
           main.Room.food -= 2
        elif main.Room.food > 0:
           main.Room.medkit += 1
           main.Room.water += 2
           main.Room.food = 0
        messagebox.showinfo(message="Исход1")
        root.destroy()

    def end2():
        messagebox.showinfo(message="Исход2")
        root.destroy()


    btn1 = Button(frame_bottom1, text="Выбор 1", bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text="Выбор 2", bg="brown", command=end2)
    btn2.pack(side=LEFT)



def event11():
    print("Условия")
    print("Выбор 1")
    print("Выбор 2")
    print("Выбор 3")

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
        if main.Room.axe > 0:
            i = random.randint(1,4)
        if i ==1:
            if main.Ted.hp >1:
                main.Ted.hp -= 1
            else:
                main.Ted.hp == 0
        elif i ==2:
            if main.Timmi.hp >1:
                main.Timmi.hp -= 1
            else:
                main.Timmi.hp == 0
        elif i ==3:
            if main.Dolores.hp >1:
                main.Dolores.hp -= 1
            else:
                main.Dolores.hp == 0
        elif i ==4:
            if main.Mary.hp >1:
                main.Mary.hp -= 1
            else:
                main.Mary.hp == 0 
        messagebox.showinfo(message="Исход2")
        root.destroy()

    def end3():
        messagebox.showinfo(message="Исход3")
        root.destroy()


    btn1 = Button(frame_bottom1, text="Выбор 1", bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text="Выбор 2", bg="brown", command=end2)
    btn2.pack(side=LEFT)

    btn3 = Button(frame_bottom1, text="Выбор 3", bg="brown", command=end3)
    btn3.pack(side=LEFT)


def event12():
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
        if main.Room.water > 2:
            main.Room.water -= 2
        elif main.Room.water > 0:
            main.Room.water = 0
            main.Room.medkit += 1
            main.Room.food += 2
        messagebox.showinfo(message="Исход1")
        root.destroy()

    def end2():
        messagebox.showinfo(message="Исход2")
        root.destroy()


    btn1 = Button(frame_bottom1, text="Выбор 1", bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text="Выбор 2", bg="brown", command=end2)
    btn2.pack(side=LEFT)


def day1():
    print("Текст день 1")
    if main.Ted.hunger == 0 or main.Ted.thrust == 0 or main.Ted.hp == 0:
        main.Ted.__del__()
        print("Tед мертв")
    if main.Dolores.hunger == 0 or main.Dolores.thrust == 0 or main.Dolores.hp == 0:
        main.Dolores.__del__()
        print("Доллорес мертва")
    if main.Timmi.hunger == 0 or main.Timmi.thrust == 0 or main.Timmi.hp == 0:
        main.Timmi.__del__()
        print("Тимми мертв")
    if main.Mary.hunger == 0 or main.Mary.thrust == 0 or main.Mary.hp == 0:
        main.Mary.__del__()
        print("Мари мертва")
    main.day_start()

    i = random.randint(1,12)
    if i == 1:
        event1()
    elif i == 2:
        event2()
    elif i == 3:
        event3()        
    elif i == 4:
        event4()
    elif i == 5:
        event5()
    elif i == 6:
        event6()
    elif i == 7:
        event7()
    elif i == 8:
        event8()
    elif i == 9:
        event9()
    elif i == 10:
        event10()
    elif i == 11:
        event11()
    elif i == 12:
        event12()

    root = Tk()
    root.title("Событие")
    root.geometry("300x100")

    frame_top = Frame(root)
    frame_top.pack(side=TOP)

    frame_bottom1 = Frame(root, bg="white")
    frame_bottom1.pack(side=BOTTOM)

    def end1():
        messagebox.showinfo(message="Исход1")
        root.destroy()
        day2()


    def end2():
        messagebox.showinfo(message="Исход2")
        root.destroy()
        day2()

    def end3():
        i = random.randint(1,4)
        if i ==1:
            main.Ted.hp -= 2
        elif i ==2:
            main.Timmi.hp -= 2
        elif i ==3:
            main.Dolores.hp -= 2
        elif i ==4:
            main.Mary.hp -= 2        
        messagebox.showinfo(message="Исход3")
        root.destroy()
        day2()

    btn1 = Button(frame_bottom1, text="Выбор 1", bg="brown", command=end1)
    btn1.pack(side=main.LEFT)

    btn2 = Button(frame_bottom1, text="Выбор 2", bg="brown", command=end2)
    btn2.pack(side=main.LEFT)

    btn3 = main.Button(frame_bottom1, text="Выбор 3", bg="brown", command=end3)
    btn3.pack(side=main.LEFT)

def day2():
    print("Текст день 2")
    if main.Ted.hunger == 0 or main.Ted.thrust == 0 or main.Ted.hp == 0:
        main.Ted.__del__()
        print("Tед мертв")
    if main.Dolores.hunger == 0 or main.Dolores.thrust == 0 or main.Dolores.hp == 0:
        main.Dolores.__del__()
        print("Доллорес мертва")
    if main.Timmi.hunger == 0 or main.Timmi.thrust == 0 or main.Timmi.hp == 0:
        main.Timmi.__del__()
        print("Тимми мертв")
    if main.Mary.hunger == 0 or main.Mary.thrust == 0 or main.Mary.hp == 0:
        main.Mary.__del__()
        print("Мари мертва")
    main.day_start()

    i = random.randint(1,12)
    if i == 1:
        event1()
    elif i == 2:
        event2()
    elif i == 3:
        event3()        
    elif i == 4:
        event4()
    elif i == 5:
        event5()
    elif i == 6:
        event6()
    elif i == 7:
        event7()
    elif i == 8:
        event8()
    elif i == 9:
        event9()
    elif i == 10:
        event10()
    elif i == 11:
        event11()
    elif i == 12:
        event12()

    root = Tk()
    root.title("Событие")
    root.geometry("100x100")

    frame_top = Frame(root)
    frame_top.pack(side=TOP)

    frame_bottom1 = Frame(root, bg="white")
    frame_bottom1.pack(side=BOTTOM)


    def end1():
        main.Room.food += 1
        main.Room.water += 1
        messagebox.showinfo(message="Исход1")
        root.destroy()
        day3()


    def end2():
        messagebox.showinfo(message="Исход2")
        root.destroy()
        day3()


    btn1 = Button(frame_bottom1, text="Выбор 1", bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text="Выбор 2", bg="brown", command=end2)
    btn2.pack(side=LEFT)


def day3():
    print("Текст день 1")
    if main.Ted.hunger == 0 or main.Ted.thrust == 0 or main.Ted.hp == 0:
        main.Ted.__del__()
        print("Tед мертв")
    if main.Dolores.hunger == 0 or main.Dolores.thrust == 0 or main.Dolores.hp == 0:
        main.Dolores.__del__()
        print("Доллорес мертва")
    if main.Timmi.hunger == 0 or main.Timmi.thrust == 0 or main.Timmi.hp == 0:
        main.Timmi.__del__()
        print("Тимми мертв")
    if main.Mary.hunger == 0 or main.Mary.thrust == 0 or main.Mary.hp == 0:
        main.Mary.__del__()
        print("Мари мертва")
    main.day_start()

    i = random.randint(1,12)
    if i == 1:
        event1()
    elif i == 2:
        event2()
    elif i == 3:
        event3()        
    elif i == 4:
        event4()
    elif i == 5:
        event5()
    elif i == 6:
        event6()
    elif i == 7:
        event7()
    elif i == 8:
        event8()
    elif i == 9:
        event9()
    elif i == 10:
        event10()
    elif i == 11:
        event11()
    elif i == 12:
        event12()

    day4()

def day4():
    print("Текст день 4")
    if main.Ted.hunger == 0 or main.Ted.thrust == 0 or main.Ted.hp == 0:
        main.Ted.__del__()
        print("Tед мертв")
    if main.Dolores.hunger == 0 or main.Dolores.thrust == 0 or main.Dolores.hp == 0:
        main.Dolores.__del__()
        print("Доллорес мертва")
    if main.Timmi.hunger == 0 or main.Timmi.thrust == 0 or main.Timmi.hp == 0:
        main.Timmi.__del__()
        print("Тимми мертв")
    if main.Mary.hunger == 0 or main.Mary.thrust == 0 or main.Mary.hp == 0:
        main.Mary.__del__()
        print("Мари мертва")
    main.day_start()

    i = random.randint(1,12)
    if i == 1:
        event1()
    elif i == 2:
        event2()
    elif i == 3:
        event3()        
    elif i == 4:
        event4()
    elif i == 5:
        event5()
    elif i == 6:
        event6()
    elif i == 7:
        event7()
    elif i == 8:
        event8()
    elif i == 9:
        event9()
    elif i == 10:
        event10()
    elif i == 11:
        event11()
    elif i == 12:
        event12()

    root = Tk()
    root.title("Событие")
    root.geometry("300x100")

    frame_top = Frame(root)
    frame_top.pack(side=TOP)

    frame_bottom1 = Frame(root, bg="white")
    frame_bottom1.pack(side=BOTTOM)

    def end1():
        messagebox.showinfo(message="Исход1") #если радио есть
        root.destroy()
        day5()

    def end2():
        messagebox.showinfo(message="Исход2")
        root.destroy()
        day5()

    btn1 = Button(frame_bottom1, text="Выбор 1", bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text="Выбор 2", bg="brown", command=end2)
    btn2.pack(side=LEFT)

def day5():
    print("Текст день 1")
    if main.Ted.hunger == 0 or main.Ted.thrust == 0 or main.Ted.hp == 0:
        main.Ted.__del__()
        print("Tед мертв")
    if main.Dolores.hunger == 0 or main.Dolores.thrust == 0 or main.Dolores.hp == 0:
        main.Dolores.__del__()
        print("Доллорес мертва")
    if main.Timmi.hunger == 0 or main.Timmi.thrust == 0 or main.Timmi.hp == 0:
        main.Timmi.__del__()
        print("Тимми мертв")
    if main.Mary.hunger == 0 or main.Mary.thrust == 0 or main.Mary.hp == 0:
        main.Mary.__del__()
        print("Мари мертва")
    main.day_start()

    i = random.randint(1,12)
    if i == 1:
        event1()
    elif i == 2:
        event2()
    elif i == 3:
        event3()        
    elif i == 4:
        event4()
    elif i == 5:
        event5()
    elif i == 6:
        event6()
    elif i == 7:
        event7()
    elif i == 8:
        event8()
    elif i == 9:
        event9()
    elif i == 10:
        event10()
    elif i == 11:
        event11()
    elif i == 12:
        event12()

    day6()

def day6():
    print("Текст день 1")
    if main.Ted.hunger == 0 or main.Ted.thrust == 0 or main.Ted.hp == 0:
        main.Ted.__del__()
        print("Tед мертв")
    if main.Dolores.hunger == 0 or main.Dolores.thrust == 0 or main.Dolores.hp == 0:
        main.Dolores.__del__()
        print("Доллорес мертва")
    if main.Timmi.hunger == 0 or main.Timmi.thrust == 0 or main.Timmi.hp == 0:
        main.Timmi.__del__()
        print("Тимми мертв")
    if main.Mary.hunger == 0 or main.Mary.thrust == 0 or main.Mary.hp == 0:
        main.Mary.__del__()
        print("Мари мертва")
    main.day_start()

    i = random.randint(1,12)
    if i == 1:
        event1()
    elif i == 2:
        event2()
    elif i == 3:
        event3()        
    elif i == 4:
        event4()
    elif i == 5:
        event5()
    elif i == 6:
        event6()
    elif i == 7:
        event7()
    elif i == 8:
        event8()
    elif i == 9:
        event9()
    elif i == 10:
        event10()
    elif i == 11:
        event11()
    elif i == 12:
        event12()

    day7

def day7():
    print("Текст день 1")
    if main.Ted.hunger == 0 or main.Ted.thrust == 0 or main.Ted.hp == 0:
        main.Ted.__del__()
        print("Tед мертв")
    if main.Dolores.hunger == 0 or main.Dolores.thrust == 0 or main.Dolores.hp == 0:
        main.Dolores.__del__()
        print("Доллорес мертва")
    if main.Timmi.hunger == 0 or main.Timmi.thrust == 0 or main.Timmi.hp == 0:
        main.Timmi.__del__()
        print("Тимми мертв")
    if main.Mary.hunger == 0 or main.Mary.thrust == 0 or main.Mary.hp == 0:
        main.Mary.__del__()
        print("Мари мертва")
    main.day_start()

    i = random.randint(1,12)
    if i == 1:
        event1()
    elif i == 2:
        event2()
    elif i == 3:
        event3()        
    elif i == 4:
        event4()
    elif i == 5:
        event5()
    elif i == 6:
        event6()
    elif i == 7:
        event7()
    elif i == 8:
        event8()
    elif i == 9:
        event9()
    elif i == 10:
        event10()
    elif i == 11:
        event11()
    elif i == 12:
        event12()

    day8()

def day8():
    print("Текст день 1")
    if main.Ted.hunger == 0 or main.Ted.thrust == 0 or main.Ted.hp == 0:
        main.Ted.__del__()
        print("Tед мертв")
    if main.Dolores.hunger == 0 or main.Dolores.thrust == 0 or main.Dolores.hp == 0:
        main.Dolores.__del__()
        print("Доллорес мертва")
    if main.Timmi.hunger == 0 or main.Timmi.thrust == 0 or main.Timmi.hp == 0:
        main.Timmi.__del__()
        print("Тимми мертв")
    if main.Mary.hunger == 0 or main.Mary.thrust == 0 or main.Mary.hp == 0:
        main.Mary.__del__()
        print("Мари мертва")
    main.day_start()

    i = random.randint(1,12)
    if i == 1:
        event1()
    elif i == 2:
        event2()
    elif i == 3:
        event3()        
    elif i == 4:
        event4()
    elif i == 5:
        event5()
    elif i == 6:
        event6()
    elif i == 7:
        event7()
    elif i == 8:
        event8()
    elif i == 9:
        event9()
    elif i == 10:
        event10()
    elif i == 11:
        event11()
    elif i == 12:
        event12()

    day9()

def day9():
    print("Текст день 9")
    if main.Ted.hunger == 0 or main.Ted.thrust == 0 or main.Ted.hp == 0:
        main.Ted.__del__()
        print("Tед мертв")
    if main.Dolores.hunger == 0 or main.Dolores.thrust == 0 or main.Dolores.hp == 0:
        main.Dolores.__del__()
        print("Доллорес мертва")
    if main.Timmi.hunger == 0 or main.Timmi.thrust == 0 or main.Timmi.hp == 0:
        main.Timmi.__del__()
        print("Тимми мертв")
    if main.Mary.hunger == 0 or main.Mary.thrust == 0 or main.Mary.hp == 0:
        main.Mary.__del__()
        print("Мари мертва")
    main.day_start()

    i = random.randint(1,12)
    if i == 1:
        event1()
    elif i == 2:
        event2()
    elif i == 3:
        event3()        
    elif i == 4:
        event4()
    elif i == 5:
        event5()
    elif i == 6:
        event6()
    elif i == 7:
        event7()
    elif i == 8:
        event8()
    elif i == 9:
        event9()
    elif i == 10:
        event10()
    elif i == 11:
        event11()
    elif i == 12:
        event12()

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
        day10()

    def end2():
        messagebox.showinfo(message="Исход2")
        root.destroy()
        day10()

    btn1 = Button(frame_bottom1, text="Выбор 1", bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text="Выбор 2", bg="brown", command=end2)
    btn2.pack(side=LEFT)


def day10():
    print("Текст день 10")
    if main.Ted.hunger == 0 or main.Ted.thrust == 0 or main.Ted.hp == 0:
        main.Ted.__del__()
        print("Tед мертв")
    if main.Dolores.hunger == 0 or main.Dolores.thrust == 0 or main.Dolores.hp == 0:
        main.Dolores.__del__()
        print("Доллорес мертва")
    if main.Timmi.hunger == 0 or main.Timmi.thrust == 0 or main.Timmi.hp == 0:
        main.Timmi.__del__()
        print("Тимми мертв")
    if main.Mary.hunger == 0 or main.Mary.thrust == 0 or main.Mary.hp == 0:
        main.Mary.__del__()
        print("Мари мертва")
    main.day_start()

    i = random.randint(1,12)
    if i == 1:
        event1()
    elif i == 2:
        event2()
    elif i == 3:
        event3()        
    elif i == 4:
        event4()
    elif i == 5:
        event5()
    elif i == 6:
        event6()
    elif i == 7:
        event7()
    elif i == 8:
        event8()
    elif i == 9:
        event9()
    elif i == 10:
        event10()
    elif i == 11:
        event11()
    elif i == 12:
        event12()

    root = Tk()
    root.title("Событие")
    root.geometry("300x100")

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


    btn1 = Button(frame_bottom1, text="Выбор 1", bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text="Выбор 2", bg="brown", command=end2)
    btn2.pack(side=LEFT)

def btn_click():
    hp = main.Ted.hp
    inventory = main.Ted.inventory
    hunger = main.Ted.hunger
    thrust = main.Ted.thrust
    info = f"{str(hp)} ted's hp, {str(inventory)} ted's inventory, {str(hunger)} ted's, {str(thrust)} ted's"
    messagebox.showerror(title="ted", message=info)


def btn1_click():
    event2()


root = Tk()
root.title("Игра")
root.geometry("300x250")


frame = Frame(root)
frame.place(relx=0, rely=0, relwidth=1, relheight=1)


btn2 = Button(frame, text="Следующий день", bg="red", command=day1)
btn2.pack(side=BOTTOM)

root.mainloop()