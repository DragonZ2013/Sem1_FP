from tkinter import *
from Functions.Hotel import *

"""
Mach eine Reservierung•
Anzeige die Liste von Gästen, die aktuelle Reservierungen haben
•Anzeige alle Zimmer gefiltert mit Preis und Meerblick Kriterien 
Anzeige alle Zimmer, die heute frei sind"""


class GuiRes:
    def __init__(self,  root_window):
        self.__window = root_window
        # self.__controller = controller

        self.__gast_vorname_txt = Entry(self.__window, width=50)
        self.__gast_nachname_txt = Entry(self.__window, width=50)

    def create_window(self):
        self.__window.title('Menu Zimmer')
        self.__window.geometry("900x900")

    def create_menu(self):
        my_menu = Menu(self.__window)
        self.__window.config(menu=my_menu)
        my_menu.add_command(label="Mach eine Reservierung")
        my_menu.add_command(label='Anzeige die Liste von Gästen, die aktuelle Reservierungen haben')
        my_menu.add_command(label='Anzeige alle Zimmer gefiltert mit Preis und Meerblick Kriterien ')
        my_menu.add_command(label='Anzeige alle Zimmer, die heute frei sind')
        file_menu = Menu(my_menu)
        my_menu.add_cascade(label='File Menu', menu=file_menu)
        file_menu.add_command(label='Help')
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.__window.destroy)

    def doallofit(self):
        self.create_window()
        self.create_menu()
