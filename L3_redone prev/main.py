from UI.Menu import menu
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


'''
def main():


    class Root(Tk):
        def __init__(self):
            super(Root, self).__init__()
            self.title("Python Tkinter Dialog Widget")
            self.minsize(640, 400)
            #self.wm_iconbitmap('icon.ico')

            self.labelFrame = ttk.LabelFrame(self, text="Open File")
            self.labelFrame.grid(column=0, row=1, padx=20, pady=20)

            self.button()

        def button(self):
            self.button = ttk.Button(self.labelFrame, text="Browse A File", command=self.fileDialog)
            self.button.grid(column=1, row=1)

        def fileDialog(self):
            self.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=
            ( ("All files", "*.*"), ("Text files", "*.txt")))
            print(self.filename)
            self.label = ttk.Label(self.labelFrame, text="")
            self.label.grid(column=1, row=2)
            self.label.configure(text=self.filename)

    #root = Root()
    #root.mainloop()
    

main()'''
menu()
'''
from UI.GUI_Reserv import *
from UI.GUI_Room import *
from UI.GUI_Guest import *
from Functions.Hotel import *
from tkinter import *
class GUIG:
    def __init__(self, root_window):
        # self.__controller = controller
        self.__window = root_window
        self.__Hotel = Hotel()


    def create_window(self):
        self.__window.title('Mein Hotel')
        self.__window.geometry("900x900")

    def open_new_window(self, window_name, clasa):  # window_name va fi menu_gaste/menu_zimmer/menu_res(string)
        new_window = Toplevel()
        new_window.title(window_name)
        menu = clasa(new_window)
        menu.doallofit()

    def create_menu(self):

        my_menu = Menu(self.__window)

        my_menu.add_command(label="Menu Gaste", command=lambda: self.open_new_window('Menu Gaste', GuiGuest))
        my_menu.add_command(label='Menu Zimmer', command=lambda: self.open_new_window('Menu Zimmer', GuiRoom))
        my_menu.add_command(label='Menu Reservierungen', command=lambda: self.open_new_window('Menu Reservierungen',GuiRes))

        file_menu = Menu(my_menu)
        my_menu.add_cascade(label="File Menu", menu=file_menu)

        file_menu.add_command(label='Exit', command=self.__window.quit)
        file_menu.add_separator()
        file_menu.add_command(label='Help'),  # command=ceva
        self.__window.config(menu=my_menu)

    def doallofit(self):
        self.create_window()
        self.create_menu()


def main():
    root = Tk()
    creation = GUIG(root)
    creation.doallofit()
    label = Label(root, text="Test text")
    label.pack()
    root.mainloop()


main()'''
