from Functions.Hotel import *
#from datetime import datetime
# from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
def pick_in_file():
    return askopenfilename(initialdir=r"D:\Projects\Python\L3_redone", title="Select the input file", filetype=
    (("Text files", "*.txt"),
     ("All files", "*.*")))  # show an "Open" dialog box and return the path to the selected file
def pick_out_file():
    return askopenfilename(initialdir=r"D:\Projects\Python\L3_redone", title="Select the output file", filetype=
    (("Text files", "*.txt"),
     ("All files", "*.*")))  # show an "Open" dialog box and return the path to the selected file


max_id = 0
def loadFromFile(Func,Filename):

    #gaste_file = open("Gaste_File.txt", 'r')
    #room_file = open("Room_File.txt", 'r')
    #reserv_file = open("Reserv_File.txt", 'r')
    all_file = open(Filename,'r')
    i=0


    def read_room(line):
        info = line.split(";")
        temp = Room(int(info[0]), int(info[1]), int(info[2]), str(info[3]), int(info[4]))
        Funct.add_room(temp)
    #room_file.close()

    def read_guest(line):
        info=line.split(";")

        info[2]=info[2].replace(' ','')
        info[2]=info[2].replace('[','')
        info[2]=info[2].replace(']','')
        info[2]=info[2].replace('\n','')
        li = info[2].split(",")
        if info[2]:
            for i in range(0,len(li)):
                li[i]=int(li[i])
        else:
            li=[]

        temp=Gaste(str(info[0]),str(info[1]),li)
        Funct.add_guest(temp)

    #gaste_file.close()
    def read_reserv(line):
        info = line.split(";")
        global max_id
        if int(info[0])>max_id:
            max_id=int(info[0])
        li2=[]
        li = info[1].replace(' ', '')
        li = li.replace('[', '')
        li = li.replace(']', '')
        li = li.replace('\n', '')
        li= li.split(",")

        for el in li:
            el=el.split(":")
            li2.append(Funct.guest_by_name(el[0],el[1]))
        info[3]=info[3].split("-")
        info[4]=info[4].split("-")
        #print(Funct.room_by_number(int(info[2])))
        temp=Reserv(int(info[0]),li2,Funct.room_by_number(int(info[2])),
                    datetime(int(info[3][2]),int(info[3][1]),int(info[3][0])),
                    datetime(int(info[4][2]),int(info[4][1]),int(info[4][0])))
        Funct.make_reserv_existing(temp)
    #reserv_file.close()
    for el in Funct.guests:
        for i in range(0,len(el.reserv)):
            el.reserv[i] = Funct.reserv_by_id(el.reserv[i])
    for line in all_file:

        if line=="-\n":
            i = i + 1
        elif line=="\n":
            i=i+1
        elif i==0:
            read_room(line)
        elif i==1:
            read_guest(line)
        else:
            read_reserv(line)
    Funct.index_reserv=max_id
    all_file.close()
def saveToFile(Func,Filename):
    '''gaste_file = open("Gaste_File.txt", 'w')
    room_file = open("Room_File.txt", 'w')
    reserv_file = open("Reserv_File.txt", 'w')'''
    all_file = open(Filename,'w')
    for el in Func.rooms:
        all_file.write(str(el) + '\n')

    all_file.write('-'+'\n')
    for el in Func.guests:
        all_file.write(str(el) + '\n')
    all_file.write('-' + '\n')
    for el in Func.reservs:
        all_file.write(str(el) + '\n')


Funct = Hotel()
loadFromFile(Funct,pick_in_file())
#guest1 = Gaste("Bob", "Derryl", [])
#guest2 = Gaste("Emil", "Dorel", [])
#Funct.add_guest(guest1)
#Funct.add_guest(guest2)
#room1 = Room(1, 3, 200, "Rot", 0)
#room2 = Room(2, 2, 150, "Grun", 1)
#Funct.add_room(room1)
#Funct.add_room(room2)
#reserv1 = Reserv(1, [Funct.guests[0], Funct.guests[1]], Funct.rooms[0], datetime(2020, 11, 21), datetime(2020, 11, 24))
#reserv2 = Reserv(2, [Funct.guests[0], Funct.guests[1]], Funct.rooms[0], datetime(2020, 11, 25), datetime(2020, 11, 27))

#Funct.make_reserv_existing(reserv1)
#Funct.make_reserv_existing(reserv2)


def recall(x):#returns the user on the main menu if x==1
    if x == 1:
        menu()
    else:
        saveToFile(Funct,pick_out_file())
        return 0

#Menu Gaste
def a():
    print(
        '1. Füge ein neuer Gast hin\n2. Aktualisierung der Nachname eines Gastes\n3. Löschung eines Gastes\n4. Anzeige die Liste von Gästen\n0. Exit')
    N = int(input("Option:"))

    if N == 1:
        Funct.add_guest_input()
        print("Der Gast wurde hinzugefügt. Möchten Sie andere Operationen ausführen? (0 - nein, 1 - ja)")
        x = int(input())
        recall(x)

    elif N == 2:
        Funct.change_guest_name_input()
        print("Der Name des Gastes wurde geändert. Möchten Sie andere Operationen durchführen? (0 - nein, 1 - ja)")
        x = int(input())
        recall(x)

    elif N == 3:
        Funct.del_guest_input()
        print("Der Gast wurde gelöscht. Möchten Sie andere Operationen ausführen? (0 - nein, 1 - ja)")
        x = int(input())
        recall(x)

    elif N == 4:
        Funct.show_guests()
        print("Möchten Sie andere Operationen durchführen? (0 - nein, 1 - ja)")
        x = int(input())
        recall(x)

    elif N == 0:
        recall(1)

    else:
        print("Ungultige Ziffer")
        a()

#Menu Zimmern
def b():
    print(
        '1. Füge ein Zimmer hin\n2. Aktualisierung des Preises eines Zimmers\n3. Löschung eines Zimmers\n4. Anzeige die Liste von Zimmern\n0. Exit')
    N = int(input("Option:"))

    if N == 1:
        Funct.add_room_input()
        print("Die Kamera wurde hinzugefügt. Möchten Sie andere Vorgänge ausführen? (0 - nein, 1 - ja)")
        x = int(input())
        recall(x)

    elif N == 2:
        Funct.change_room_cost_input()
        print("Der Preis des Zimmers wurde geändert. Möchten Sie andere Operationen durchführen? (0 - nein, 1 - ja)")
        x = int(input())
        recall(x)

    elif N == 3:
        Funct.del_room_input()
        print("Die Kamera war Stears, möchten Sie andere Operationen durchführen? (0 - nein, 1 - ja)")
        x = int(input())
        recall(x)

    elif N == 4:
        Funct.show_rooms()
        print("Möchten Sie andere Operationen durchführen? (0 - nein, 1 - ja)")
        x = int(input())
        recall(x)

    elif N == 0:
        recall(1)

    else:
        print("Ungultige Ziffer")
        b()

#Menu Gemeinsam
def c():
    print(
        '1. Mach eine Reservierung\n2. Anzeige die Liste von Gästen, die aktuelle Reservierungen haben\n3. Anzeige alle Zimmer gefiltert mit Preis und Meerblick Kriterien (z. B. ein Zimmer billiger als 100 Euro, mit Meerblick)\n4. Anzeige alle Zimmer, die heute frei sind\n5. Anzeige alle Reservierung\n 0. Exit')
    N = int(input("Option:"))

    if N == 1:
        Funct.make_reserv_input()
        print("Möchten Sie andere Operationen durchführen? (0 - nein, 1 - ja)")
        x = int(input())
        recall(x)

    elif N == 2:
        x = int(input(
            "Verwenden Sie das aktuelle Datum oder geben Sie es über die Tastatur ein? (0 - aktuell, 1 - eingegeben):"))
        if x == 1:
            data = datetime.strptime(str(input("Data DD-MM-YYYY: ")), '%d-%m-%Y')
            Funct.guest_today(data)
        else:
            Funct.guest_today()
        print("Möchten Sie andere Operationen durchführen? (0 - nein, 1 - ja)")
        x = int(input())
        recall(x)

    elif N == 3:
        Funct.show_room_filter_input()
        print("Möchten Sie andere Operationen durchführen? (0 - nein, 1 - ja)")
        x = int(input())
        recall(x)

    elif N == 4:
        x = int(input(
            "Verwenden Sie das aktuelle Datum oder geben Sie es über die Tastatur ein? (0 - aktuell, 1 - eingegeben):"))
        if x == 1:
            data = datetime.strptime(str(input("Data DD-MM-YYYY: ")), '%d-%m-%Y')
            Funct.free_today(data)
        else:
            Funct.free_today()
        print("Möchten Sie andere Operationen durchführen? (0 - nein, 1 - ja)")
        x = int(input())
        recall(x)

    elif N == 5:
        Funct.show_reservs()
        print("Möchten Sie andere Operationen durchführen? (0 - nein, 1 - ja)")
        x = int(input())
        recall(x)

    elif N == 0:
        recall(1)
    else:
        print("Ungultige Ziffer")
        c()


def menu():
    print("1. Menu Gäste\n2. Menu Zimmern\n3. Menu Gemeinsam\n0. Exit")
    n = int(input("Option:"))
    if n == 1:
        a()
    elif n == 2:
        b()
    elif n == 3:
        c()
    elif n == 0:
        saveToFile(Funct,pick_out_file())
        return
    else:
        print("Ungultige Ziffer")
        menu()
