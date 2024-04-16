# Case-study #5
# Developers: Borodin Artemiy, Solovyova Maria,
# Selikhova Polina, Lyamin Egor
#

import main as main
from tkinter import *
from tkinter import messagebox
import ru_local as ru
import random


def event_random():
    """
    random events function
    """
    i = random.randint(1, 12)
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


def event1():
    print(ru.EVENT_1)
    print(ru.EVENT_1_1)
    print(ru.EVENT_1_2)
    root = Tk()
    root.title(ru.EVENT_1)
    root.geometry("500x500")

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
    root.geometry("500x500")

    frame_top = Frame(root)
    frame_top.pack(side=TOP)

    frame_bottom1 = Frame(root, bg="white")
    frame_bottom1.pack(side=BOTTOM)

    def end1():
        if main.Room.soap > 0:
            main.Room.soap -= 1
        messagebox.showinfo(message=ru.EVENT_2_YES)
        root.destroy()

    def end2():
        if main.Room.dihlofos > 0:
            main.Room.dihlofos -= 1
        i = random.randint(1, 4)
        if i == 1:
            if main.Ted.hp > 2:
                main.Ted.hp -= 2
            else:
                main.Ted.hp == 0
        elif i == 2:
            if main.Timmi.hp > 2:
                main.Timmi.hp -= 2
            else:
                main.Timmi.hp == 0
        elif i == 3:
            if main.Dolores.hp > 2:
                main.Dolores.hp -= 2
            else:
                main.Dolores.hp == 0
        elif i == 4:
            if main.Mary.hp > 2:
                main.Mary.hp -= 2
            else:
                main.Mary.hp == 0
        messagebox.showinfo(message=ru.EVENT_2_DICHLORVOS)
        root.destroy()

    def end4():
        if main.Room.water > 0:
            main.Room.water -= 1
        messagebox.showinfo(message=ru.EVENT_2_YES)
        root.destroy()

    def end5():
        if main.Room.map > 0:
            main.Room.map -= 1
        main.Room.axe += 1
        main.Room.food += 4
        messagebox.showinfo(message=ru.EVENT_2_YES)
        root.destroy()

    def end6():
        if main.Room.map > 0:
            main.Room.map -= 1
        if main.Room.water > 4:
            main.Room.water -= 4
        elif main.Room.water > 0:
            main.Room.water = 0
        if main.Room.food > 4:
            main.Room.food -= 4
        elif main.Room.food > 0:
            main.Room.food = 0
        messagebox.showinfo(message=ru.EVENT_2_NO)
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
    print(ru.EVENT_3)
    print(ru.EVENT_3_1)
    print(ru.EVENT_3_2)
    print(ru.EVENT_3_3)
    print(ru.EVENT_3_4)
    root = Tk()
    root.title(ru.EVENT_3)
    root.geometry("500x500")

    frame_top = Frame(root)
    frame_top.pack(side=TOP)

    frame_bottom1 = Frame(root, bg="white")
    frame_bottom1.pack(side=BOTTOM)

    def end1():
        messagebox.showinfo(message=ru.EVENT_3_AXE)
        root.destroy()

    def end2():
        messagebox.showinfo(message=ru.EVENT_3_ENTERTAINMENT)
        root.destroy()

    def end3():
        messagebox.showinfo(message=ru.EVENT_3_ENTERTAINMENT)
        root.destroy()

    def end4():
        i = random.randint(1, 4)
        if i == 1:
            if main.Ted.hp > 1:
                main.Ted.hp -= 1
            else:
                main.Ted.hp == 0
        elif i == 2:
            if main.Timmi.hp > 1:
                main.Timmi.hp -= 1
            else:
                main.Timmi.hp == 0
        elif i == 3:
            if main.Dolores.hp > 1:
                main.Dolores.hp -= 1
            else:
                main.Dolores.hp == 0
        elif i == 4:
            if main.Mary.hp > 1:
                main.Mary.hp -= 1
            else:
                main.Mary.hp == 0
        messagebox.showinfo(message=ru.EVENT_3_NO)
        root.destroy()

    btn1 = Button(frame_bottom1, text=ru.EVENT_3_1, bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text=ru.EVENT_3_2, bg="brown", command=end2)
    btn2.pack(side=LEFT)

    btn3 = Button(frame_bottom1, text=ru.EVENT_3_3, bg="brown", command=end3)
    btn3.pack(side=LEFT)

    btn4 = Button(frame_bottom1, text=ru.EVENT_3_4, bg="brown", command=end4)
    btn4.pack(side=LEFT)


def event4():
    print(ru.EVENT_4)
    print(ru.EVENT_4_1)
    print(ru.EVENT_4_2)
    print(ru.EVENT_4_3)
    print(ru.EVENT_4_4)

    root = Tk()
    root.title(ru.EVENT_4)
    root.geometry("500x500")

    frame_top = Frame(root)
    frame_top.pack(side=TOP)

    frame_bottom1 = Frame(root, bg="white")
    frame_bottom1.pack(side=BOTTOM)

    def end1():
        if main.Room.rifel > 0:
            i = random.randint(1, 4)
            if i == 1:
                if main.Ted.hp > 1:
                    main.Ted.hp -= 1
                else:
                    main.Ted.hp == 0
            elif i == 2:
                if main.Timmi.hp > 1:
                    main.Timmi.hp -= 1
                else:
                    main.Timmi.hp == 0
            elif i == 3:
                if main.Dolores.hp > 1:
                    main.Dolores.hp -= 1
                else:
                    main.Dolores.hp == 0
            elif i == 4:
                if main.Mary.hp > 1:
                    main.Mary.hp -= 1
                else:
                    main.Mary.hp == 0
                messagebox.showinfo(message=ru.EVENT_4_GUN)
                root.destroy()

    def end2():
        messagebox.showinfo(message=ru.EVENT_4_RADIO)
        root.destroy()

    def end3():
        messagebox.showinfo(message=ru.EVENT_4_SPINNER)
        root.destroy()

    def end4():
        messagebox.showinfo(message=ru.EVENT_4_CARD)
        root.destroy()

    btn1 = Button(frame_bottom1, text=ru.EVENT_4_1, bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text=ru.EVENT_4_2, bg="brown", command=end2)
    btn2.pack(side=LEFT)

    btn3 = Button(frame_bottom1, text=ru.EVENT_4_3, bg="brown", command=end3)
    btn3.pack(side=LEFT)

    btn4 = Button(frame_bottom1, text=ru.EVENT_4_4, bg="brown", command=end4)
    btn4.pack(side=LEFT)


def event5():
    print(ru.EVENT_5)
    print(ru.EVENT_5_1)
    print(ru.EVENT_5_2)

    root = Tk()
    root.title(ru.EVENT_5)
    root.geometry("500x500")

    frame_top = Frame(root)
    frame_top.pack(side=TOP)

    frame_bottom1 = Frame(root, bg="white")
    frame_bottom1.pack(side=BOTTOM)

    def end1():
        main.Room.food += 8
        messagebox.showinfo(message=ru.EVENT_5_YES)
        root.destroy()

    def end2():
        messagebox.showinfo(message=ru.EVENT_NO)
        root.destroy()

    btn1 = Button(frame_bottom1, text=ru.EVENT_5_1, bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text=ru.EVENT_5_2, bg="brown", command=end2)
    btn2.pack(side=LEFT)


def event6():
    print(ru.EVENT_6)
    print(ru.EVENT_6_1)
    print(ru.EVENT_6_2)
    print(ru.EVENT_6_3)

    root = Tk()
    root.title(ru.EVENT_6)
    root.geometry("500x500")

    frame_top = Frame(root)
    frame_top.pack(side=TOP)

    frame_bottom1 = Frame(root, bg="white")
    frame_bottom1.pack(side=BOTTOM)

    def end1():
        messagebox.showinfo(message=ru.EVENT_6_FLASHLIGHT)
        root.destroy()

    def end2():
        messagebox.showinfo(message=ru.EVENT_6_BOOK)
        root.destroy()

    def end3():
        if main.Room.dihlofos > 0:
            main.Room.dihlofos -= 1
            messagebox.showinfo(message=ru.EVENT_6_DICHLORVOS)
            root.destroy()

    btn1 = Button(frame_bottom1, text=ru.EVENT_6_1, bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text=ru.EVENT_6_2, bg="brown", command=end2)
    btn2.pack(side=LEFT)

    btn3 = Button(frame_bottom1, text=ru.EVENT_6_3, bg="brown", command=end3)
    btn3.pack(side=LEFT)


def event7():
    print(ru.EVENT_7)
    print(ru.EVENT_7_1)
    print(ru.EVENT_7_2)

    root = Tk()
    root.title(ru.EVENT_7)
    root.geometry("500x500")

    frame_top = Frame(root)
    frame_top.pack(side=TOP)

    frame_bottom1 = Frame(root, bg="white")
    frame_bottom1.pack(side=BOTTOM)

    def end1():
        if main.Room.ammo > 0:
            main.Room.ammo -= 1
            main.Room.food += 8
            messagebox.showinfo(message=ru.EVENT_7_YES)
            root.destroy()

    def end2():
        messagebox.showinfo(message=ru.EVENT_NO)
        root.destroy()

    btn1 = Button(frame_bottom1, text=ru.EVENT_7_1, bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text=ru.EVENT_7_2, bg="brown", command=end2)
    btn2.pack(side=LEFT)


def event8():
    print(ru.EVENT_8)
    print(ru.EVENT_8_1)
    print(ru.EVENT_8_2)
    print(ru.EVENT_8_3)

    root = Tk()
    root.title(ru.EVENT_8)
    root.geometry("500x500")

    frame_top = Frame(root)
    frame_top.pack(side=TOP)

    frame_bottom1 = Frame(root, bg="white")
    frame_bottom1.pack(side=BOTTOM)

    def end1():
        if main.Room.dihlofos > 0:
            main.Room.dihlofos -= 1
            main.Room.food += 2
            messagebox.showinfo(message=ru.EVENT_8_DICHLORVOS)
            root.destroy()

    def end2():
        if main.Room.rifel > 0:
            main.Room.food += 2
            messagebox.showinfo(message=ru.EVENT_8_DICHLORVOS)
            root.destroy()

    def end3():
        i = random.randint(1, 4)
        if i == 1:
            if main.Ted.hp > 2:
                main.Ted.hp -= 2
            else:
                main.Ted.hp == 0
        elif i == 2:
            if main.Timmi.hp > 2:
                main.Timmi.hp -= 2
            else:
                main.Timmi.hp == 0
        elif i == 3:
            if main.Dolores.hp > 2:
                main.Dolores.hp -= 2
            else:
                main.Dolores.hp == 0
        elif i == 4:
            if main.Mary.hp > 2:
                main.Mary.hp -= 2
            else:
                main.Mary.hp == 0
        messagebox.showinfo(message=ru.EVENT_8_NO)
        root.destroy()

    btn1 = Button(frame_bottom1, text=ru.EVENT_8_1, bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text=ru.EVENT_8_2, bg="brown", command=end2)
    btn2.pack(side=LEFT)

    btn3 = Button(frame_bottom1, text=ru.EVENT_8_3, bg="brown", command=end3)
    btn3.pack(side=LEFT)


def event9():
    print(ru.EVENT_9)
    print(ru.EVENT_9_1)
    print(ru.EVENT_9_2)

    root = Tk()
    root.title(ru.EVENT_9)
    root.geometry("500x500")

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
        messagebox.showinfo(message=ru.EVENT_9_YES)
        root.destroy()

    def end2():
        messagebox.showinfo(message=ru.EVENT_NO)
        root.destroy()

    btn1 = Button(frame_bottom1, text=ru.EVENT_9_1, bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text=ru.EVENT_9_2, bg="brown", command=end2)
    btn2.pack(side=LEFT)


def event10():
    print(ru.EVENT_9)
    print(ru.EVENT_9_1)
    print(ru.EVENT_9_2)

    root = Tk()
    root.title(ru.EVENT_9)
    root.geometry("500x500")

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
        messagebox.showinfo(message=ru.EVENT_9_YES)
        root.destroy()

    def end2():
        messagebox.showinfo(message=ru.EVENT_NO)
        root.destroy()

    btn1 = Button(frame_bottom1, text=ru.EVENT_9_1, bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text=ru.EVENT_9_2, bg="brown", command=end2)
    btn2.pack(side=LEFT)


def event11():
    print(ru.EVENT_10)
    print(ru.EVENT_10_1)
    print(ru.EVENT_10_2)
    print(ru.EVENT_10_3)

    root = Tk()
    root.title(ru.EVENT_10)
    root.geometry("500x500")

    frame_top = Frame(root)
    frame_top.pack(side=TOP)

    frame_bottom1 = Frame(root, bg="white")
    frame_bottom1.pack(side=BOTTOM)

    def end1():
        messagebox.showinfo(message=ru.EVENT_10_LOCK)
        root.destroy()

    def end2():
        if main.Room.axe > 0:
            i = random.randint(1, 4)
            if i == 1:
                if main.Ted.hp > 1:
                    main.Ted.hp -= 1
                else:
                    main.Ted.hp == 0
            elif i == 2:
                if main.Timmi.hp > 1:
                    main.Timmi.hp -= 1
                else:
                    main.Timmi.hp == 0
            elif i == 3:
                if main.Dolores.hp > 1:
                    main.Dolores.hp -= 1
                else:
                    main.Dolores.hp == 0
            elif i == 4:
                if main.Mary.hp > 1:
                    main.Mary.hp -= 1
                else:
                    main.Mary.hp == 0
        messagebox.showinfo(message=ru.EVENT_10_AXE)
        root.destroy()

    def end3():
        messagebox.showinfo(message=ru.EVENT_10_GUN)
        root.destroy()

    btn1 = Button(frame_bottom1, text=ru.EVENT_10_1, bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text=ru.EVENT_10_2, bg="brown", command=end2)
    btn2.pack(side=LEFT)

    btn3 = Button(frame_bottom1, text=ru.EVENT_10_3, bg="brown", command=end3)
    btn3.pack(side=LEFT)


def event12():
    print(ru.EVENT_9)
    print(ru.EVENT_9_1)
    print(ru.EVENT_9_2)

    root = Tk()
    root.title(ru.EVENT_9)
    root.geometry("500x500")

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
        messagebox.showinfo(message=ru.EVENT_9_YES)
        root.destroy()

    def end2():
        messagebox.showinfo(message=ru.EVENT_NO)
        root.destroy()

    btn1 = Button(frame_bottom1, text="Выбор 1", bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text="Выбор 2", bg="brown", command=end2)
    btn2.pack(side=LEFT)


def day1():
    print(ru.DAY_1)

    # main.exploror()

    event_random()

    root = Tk()
    root.title(ru.TEXT_1)
    root.geometry("500x500")

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
        i = random.randint(1, 4)
        if i == 1:
            main.Ted.hp -= 2
        elif i == 2:
            main.Timmi.hp -= 2
        elif i == 3:
            main.Dolores.hp -= 2
        elif i == 4:
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

    main.live()


def day2():
    print("Текст день 2")

    main.live()
    event_random()
    # main.exploror()

    root = Tk()
    root.title("Событие")
    root.geometry("500x500")

    frame_top = Frame(root)
    frame_top.pack(side=TOP)

    frame_bottom1 = Frame(root, bg="white")
    frame_bottom1.pack(side=BOTTOM)

    def end1():
        main.Room.food += 1
        main.Room.water += 1
        messagebox.showinfo(message="Исход1")
        root.destroy()
        # main.explor_result()
        day3()

    def end2():
        messagebox.showinfo(message="Исход2")
        root.destroy()
        # main.explor_result()
        day3()

    btn1 = Button(frame_bottom1, text="Выбор 1", bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text="Выбор 2", bg="brown", command=end2)
    btn2.pack(side=LEFT)


def day3():
    print("Текст день 3")

    main.live()
    event_random()
    # main.exploror()

    # main.explor_result()
    day4()


def day4():
    print("Текст день 4")

    main.live()
    event_random()
    # main.exploror()

    root = Tk()
    root.title("Событие")
    root.geometry("300x100")

    frame_top = Frame(root)
    frame_top.pack(side=TOP)

    frame_bottom1 = Frame(root, bg="white")
    frame_bottom1.pack(side=BOTTOM)

    def end1():
        messagebox.showinfo(message="Исход1")  # если радио есть
        root.destroy()
        # main.explor_result()
        day5()

    def end2():
        messagebox.showinfo(message="Исход2")
        root.destroy()
        # main.explor_result()
        day5()

    btn1 = Button(frame_bottom1, text="Выбор 1", bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text="Выбор 2", bg="brown", command=end2)
    btn2.pack(side=LEFT)


def day5():
    print("Текст день 5")

    main.live()
    event_random()
    # main.exploror()

    # main.explor_result()
    day6()


def day6():
    print("Текст день 6")

    main.live()
    event_random()
    # main.exploror()

    # main.explor_result()
    day7()


def day7():
    print("Текст день 7")

    main.live()
    event_random()
    # main.exploror()

    # main.explor_result()
    day8()


def day8():
    print("Текст день 8")

    main.live()
    event_random()
    # main.exploror()

    # main.explor_result()
    day9()


def day9():
    print("Текст день 9")

    main.live()
    event_random()
    # main.exploror()

    root = Tk()
    root.title("Событие")
    root.geometry("500x500")

    frame_top = Frame(root)
    frame_top.pack(side=TOP)

    frame_bottom1 = Frame(root, bg="white")
    frame_bottom1.pack(side=BOTTOM)

    def end1():
        messagebox.showinfo(message="Исход1")
        root.destroy()
        # main.explor_result()
        day10()

    def end2():
        messagebox.showinfo(message="Исход2")
        root.destroy()
        # main.explor_result()
        day10()

    btn1 = Button(frame_bottom1, text="Выбор 1", bg="brown", command=end1)
    btn1.pack(side=LEFT)

    btn2 = Button(frame_bottom1, text="Выбор 2", bg="brown", command=end2)
    btn2.pack(side=LEFT)


def day10():
    print("Текст день 10")

    main.live()
    event_random()
    # main.explor_result()

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


"""root = Tk()
root.title("Игра")
root.geometry("300x250")


frame = Frame(root)
frame.place(relx=0, rely=0, relwidth=1, relheight=1)


btn2 = Button(frame, text="Следующий день", bg="red", command=day1)
btn2.pack(side=BOTTOM)

root.mainloop()"""