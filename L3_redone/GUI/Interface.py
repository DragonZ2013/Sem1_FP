from tkinter import *
from Functions.Hotel import *
from Entities.Guest import *

Funct = Hotel()
'''
guest1 = Gaste("Bob", "Derryl", [])
guest2 = Gaste("Emil", "Dorel", [])
Funct.add_guest(guest1)
Funct.add_guest(guest2)
room1 = Room(1, 3, 200, "Rot", 0)
room2 = Room(2, 2, 150, "Grun", 1)
Funct.add_room(room1)
Funct.add_room(room2)
reserv1 = Reserv(1, [guest1, guest2], room1, datetime(2020, 11, 21), datetime(2020, 11, 24))
Funct.make_reserv(reserv1)
'''


class GUI:
    def __init__(self, gui_master, controller):
        self.__window = gui_master
        self.__controller = controller
        self.__roommenu = Frame(master=self.__window, borderwidth=45)
        self.__guestmenu = Frame(master=self.__window, borderwidth=45)
        self.__reservmenu = Frame(master=self.__window, borderwidth=45)
        self.__mainmenu = Frame(master=self.__window, borderwidth=45)
        self.populate_roommenu()
        self.populate_mainmenu()
        self.populate_guestmenu()
        self.populate_reservmenu()

    def add_room(self, nr, maxguest, price, color, sea_view):
        print(nr)
        print(int(maxguest))
        print(int(price))
        print(color)
        print(int(sea_view))
        room = Room(int(nr), int(maxguest), int(price), color, int(sea_view))
        self.__controller.add_room(room)

    def populate_mainmenu(self):

        btn = Button(self.__mainmenu, text='Roommenu', command=self.draw_roommenu)
        btn.grid(column=0, row=0)

        btn2 = Button(self.__mainmenu, text='Guestmenu', command=self.draw_guestmenu)
        btn2.grid(column=1, row=0)

        btn3 = Button(self.__mainmenu, text='Reservmenu', command=self.draw_reservmenu)
        btn3.grid(column=2, row=0)

        btn4 = Button(self.__mainmenu, text='Exit', command=self.__window.destroy)
        btn4.grid(column=3, row=0)


    def populate_roommenu(self):
        string1_txt = Entry(self.__roommenu, width=50)
        string2_txt = Entry(self.__roommenu, width=50)
        string3_txt = Entry(self.__roommenu, width=50)
        string4_txt = Entry(self.__roommenu, width=50)
        string5_txt = Entry(self.__roommenu, width=50)

        btn1 = Button(self.__roommenu, text='Füge ein Zimmer hin', command=lambda: self.add_room(string1_txt.get(), string2_txt.get(), string3_txt.get(), string4_txt.get(), string5_txt.get()))
        btn1.grid(column=0, row=0)

        btn2 = Button(self.__roommenu, text='Aktualisierung des Preises eines Zimmers', command=lambda: self.change_room_cost(string1_txt.get(),))
        btn2.grid(column=1, row=0)

        btn3 = Button(self.__roommenu, text='Löschung eines Zimmers', command=self.pass1())
        btn3.grid(column=2, row=0)

        btn4 = Button(self.__roommenu, text='Anzeige die Liste von Zimmern', command=self.__controller.show_rooms)
        btn4.grid(column=3, row=0)

        btn5 = Button(self.__roommenu, text='Go to main menu', command=self.draw_menu_again_roommenu)
        btn5.grid(column=4, row=0)

        nr = Label(self.__roommenu, text='nr')
        nr.grid(column=0, row=2)
        string1_txt.grid(column=1, row=2)

        maxguest = Label(self.__roommenu, text='maxguest')
        maxguest.grid(column=0, row=3)
        string2_txt.grid(column=1, row=3)

        price = Label(self.__roommenu, text='price')
        price.grid(column=0, row=4)
        string3_txt.grid(column=1, row=4)

        color = Label(self.__roommenu, text='color')
        color.grid(column=0, row=5)
        string4_txt.grid(column=1, row=5)

        sea_view = Label(self.__roommenu, text='sea_view')
        sea_view.grid(column=0, row=6)
        string5_txt.grid(column=1, row=6)

    def draw_roommenu(self):
        self.__mainmenu.pack_forget()
        self.__roommenu.pack(fill=X)


    def populate_guestmenu(self):
        self.__string1_txt = Entry(self.__guestmenu, width=50)
        self.__string2_txt = Entry(self.__guestmenu, width=50)
        self.__string3_txt = Entry(self.__guestmenu, width=50)

        btn1 = Button(self.__guestmenu, text='Füge ein neuer Gast hin', command= self.pass1)
        btn1.grid(column=0, row=0)

        btn2 = Button(self.__guestmenu, text='Aktualisierung der Name eines Gastes', command=self.pass1)
        btn2.grid(column=1, row=0)

        btn3 = Button(self.__guestmenu, text='Löschung eines Gastes', command=self.pass1)
        btn3.grid(column=2, row=0)

        btn4 = Button(self.__guestmenu, text='Anzeige die Liste von Gästen', command=self.pass1)
        btn4.grid(column=3, row=0)

        btn0 = Button(self.__guestmenu, text='Main Menu', command=self.draw_menu_again_guestmenu)
        btn0.grid(column=4, row=0)

        nachname = Label(self.__guestmenu, text='nachname')
        nachname.grid(column=0, row=2)
        self.__string1_txt.grid(column=1, row=2)

        vorname = Label(self.__guestmenu, text='vorname')
        vorname.grid(column=0, row=3)
        self.__string2_txt.grid(column=1, row=3)

        reserv = Label(self.__guestmenu, text='reserv')
        reserv.grid(column=0, row=4)
        self.__string3_txt.grid(column=1, row=4)

    def draw_guestmenu(self):
        self.__mainmenu.pack_forget()
        self.__guestmenu.pack(fill=X)

    def populate_reservmenu(self):
        string1_txt = Entry(self.__reservmenu, width=50)
        string2_txt = Entry(self.__reservmenu, width=50)
        string3_txt = Entry(self.__reservmenu, width=50)
        string4_txt = Entry(self.__reservmenu, width=50)
        string5_txt = Entry(self.__reservmenu, width=50)

        btn1 = Button(self.__reservmenu, text='Mach eine Reservierung', command= self.pass1)
        btn1.grid(column=0, row=0)

        btn2 = Button(self.__reservmenu, text='Anzeige die Liste von Gästen, die aktuelle Reservierungen haben', command=self.pass1)
        btn2.grid(column=1, row=0)

        btn3 = Button(self.__reservmenu, text='Anzeige alle Zimmer gefiltert mit Preis und Meerblick Kriterien', command=self.pass1)
        btn3.grid(column=2, row=0)

        btn4 = Button(self.__reservmenu, text='Anzeige alle Zimmer, die heute frei sind', command= self.pass1)
        btn4.grid(column=3, row=0)

        btn5 = Button(self.__reservmenu, text='Main Menu', command=self.draw_menu_again_reservmenu)
        btn5.grid(column=4, row=0)

        nr = Label(self.__reservmenu, text='nr')
        nr.grid(column=0, row=2)
        string1_txt.grid(column=1, row=2)

        guests = Label(self.__reservmenu, text='guests')
        guests.grid(column=0, row=3)
        string2_txt.grid(column=1, row=3)

        room = Label(self.__reservmenu, text='room')
        room.grid(column=0, row=4)
        string3_txt.grid(column=1, row=4)

        datestart = Label(self.__reservmenu, text='datestart')
        datestart.grid(column=0, row=5)
        string4_txt.grid(column=1, row=5)

        datefin = Label(self.__reservmenu, text='datefin')
        datefin.grid(column=0, row=6)
        string5_txt.grid(column=1, row=6)

    def draw_reservmenu(self):
        self.__mainmenu.pack_forget()
        self.__reservmenu.pack(fill=X)

    def draw_menu_again_roommenu(self):
        self.__roommenu.pack_forget()
        self.__mainmenu.pack(fill=X)

    def draw_menu_again_guestmenu(self):
        self.__guestmenu.pack_forget()
        self.__mainmenu.pack(fill=X)

    def draw_menu_again_reservmenu(self):
        self.__reservmenu.pack_forget()
        self.__mainmenu.pack(fill=X)

    def draw_menu(self):
        self.__mainmenu.pack(fill=X)

    def pass1(self):
        pass

'''
    def __add_guest(self):
        s1 = self.__string1_txt.get()
        s2 = self.__string2_txt.get()
        # print(s1)
        # print(s2)
        g = Gaste(str(s1), str(s2), [])
        print(g)
        Funct.add_guest(g)

        # clear textboxes
        self.__string1_txt.delete(0, 'end')
        self.__string2_txt.delete(0, 'end')
'''