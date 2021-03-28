from GUI.Interface import GUI
from tkinter import *
from Functions.Hotel import Hotel
from Entities.Guest import *
from Entities.Reservation import *
from Entities.Room import *
from datetime import datetime


def main():
    
     controller = Hotel()
     guest1 = Gaste("Bob", "Derryl", [])
     guest2 = Gaste("Emil", "Dorel", [])
     controller.add_guest(guest1)
     controller.add_guest(guest2)
     room1 = Room(1, 3, 200, "Rot", 0)
     room2 = Room(2, 2, 150, "Grun", 1)
     controller.add_room(room1)
     controller.add_room(room2)
     reserv1 = Reserv(1, [guest1, guest2], room1, datetime(2020, 11, 21), datetime(2020, 11, 24))
     controller.make_reserv(reserv1)

     root = Tk()
     g = GUI(root, controller)
     g.draw_menu()
     root.mainloop()  # BLOCKS
     '''
     root = Tk()
     g = GUI(root, controller)
     frame = Frame(root)
     Grid.rowconfigure(root, 0, weight=1)
     Grid.columnconfigure(root, 0, weight=1)
     frame.grid(row=0, column=0, sticky=N + S + E + W)
     grid = Frame(frame)
     grid.grid(sticky=N + S + E + W, column=0, row=7, columnspan=2)
     Grid.rowconfigure(frame, 7, weight=1)
     Grid.columnconfigure(frame, 0, weight=1)

     # example values
     for x in range(10):
          for y in range(5):
               btn = Button(frame)
               btn.grid(column=x, row=y, sticky=N + S + E + W)

     for x in range(10):
          Grid.columnconfigure(frame, x, weight=1)

     for y in range(5):
          Grid.rowconfigure(frame, y, weight=1)

     root.mainloop()
     '''
     


main()