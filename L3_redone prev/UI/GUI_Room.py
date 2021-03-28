from tkinter import *
from Functions.Hotel import *


class GuiRoom:
    def __init__(self,  root_window):
        self.__window = root_window
        # self.__controller = controller

        self.__gast_vorname_txt = Entry(self.__window, width=50)
        self.__gast_nachname_txt = Entry(self.__window, width=50)

    def create_window(self):
        self.__window.title('Menu Reservierung')
        self.__window.geometry("900x900")

    def create_menu(self):
        my_menu = Menu(self.__window)
        self.__window.config(menu=my_menu)
        my_menu.add_command(label="Gaste einfugen")  #command=add_gast(liste_gaste))
        my_menu.add_command(label='Aktualisiere Nachname')  # command=aktualisiere(liste_gaste))
        my_menu.add_command(label='Losche Gast') # command=loschen_eines_gastes(liste_gaste))
        my_menu.add_command(label='Zeige die Liste von Gasten') # command=print_liste_gaste(liste_gaste))
        file_menu = Menu(my_menu)
        my_menu.add_cascade(label='File Menu', menu=file_menu)
        file_menu.add_command(label='Help')
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.__window.destroy)

    def doallofit(self):
        self.create_window()
        self.create_menu()

"""
def main():
    liste_gaste = []
    root = Tk()
    creation = GuiGaste(root)
    creation.create_window()
    creation.create_menu(liste_gaste)
    label = Label(root, text="I really don't know what I'm doing:)")
    label.pack()
    root.mainloop()


main()
"""