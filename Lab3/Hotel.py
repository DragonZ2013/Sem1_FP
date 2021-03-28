from Reserv import Reserv
from datetime import *

class Hotel:
    def __init__(self):
        self.__index_reserv=5
        self.__guests=[]
        self.__rooms=[]
        self.__reservs=[]
    def add_guest(self,g):
        self.__guests.append(g)
    def add_room(self,r):
        self.__rooms.append(r)
    def add_reservs(self,r):
        self.__reservs.append(r)
    def change_guest_name(self,i,s):
        self.__guests[i].change_name(s)
    def del_guest(self,i):
        self.__guests.pop(i)
    def show_guests(self):
        for g in self.__guests:
            print(g)
    def change_room_cost(self,i,val):
        self.__rooms[i].change_cost(val)
    def del_room(self,i):
        self.__room.pop(i)
    def show_rooms(self):
        for r in self.__rooms:
            print(r)
    def show_reserv_guests(self):
        for g in self.__guests:
            if g.reserv != []:
                print(g)
    def show_reservs(self):
        for r in self.__reservs:
            print(r)
    def show_room_filter(self,price,view=""):
        for r in self.__rooms:
            if r.isfilter(price,view):
                print(r)
    def room_by_number(self,x):
        for r in self.__rooms:
            if r.nr == x:
                return r

    def reserv_by_number(self,x):
        for r in self.__reservs:
            if r.nr == x:
                return r

    def del_reserv(self,x):
        r=self.reserv_by_number(x)
        self.__reservs.remove(r)
        for g in self.__guests:
            if r in g.reserv:
                g.reserv.remove(r)

    def make_reserv(self,guests,room_nr,datestart,datefin):
        ok=1
        roomc=self.room_by_number(room_nr)
        if(datefin<datestart):
            ok=0
        if roomc.maxguest<len(guests):
            ok=0
        for reservc in self.__reservs:
            if reservc.room==roomc:

                if datestart>reservc.datestart and datestart<reservc.datefin or datefin>reservc.datestart and datefin<reservc.datefin or datefin>=reservc.datefin and datestart<=reservc.datefin:
                    ok=0
        if ok==1:
            self.add_reservs(Reserv(self.__index_reserv,guests,roomc,datestart,datefin))
            for g in guests:
                g.add_reserv(Reserv(self.__index_reserv,guests,roomc,datestart,datefin))
            self.__index_reserv+=1
        else:
            print("Could not make reservation")

    def reserv_today(self,today=datetime.now()):
        for r in self.__reservs:
            if r.datestart==today or r.datestart<today and r.datefin>today:
                print(r)

    def free_today(self, today=datetime.now()):
        for room in self.__rooms:
            ok=1
            for reserv in self.__reservs:
                if reserv.room==room:
                    if(reserv.datestart<=today and reserv.datefin>=today):
                        ok=0
            if ok==1:
                print(room)