from datetime import *
from Guest import *
from Room import *
from Reserv import *
from Hotel import *




def main():
    Funct = Hotel()
    guest1=Guest(0,"Bob","Derryl",[])
    guest2=Guest(1,"Emil","Dorel",[])
    guest1.change_name("Denis")
    room1=Room(1,3,200,"Red",["Sea","Street"])
    room2=Room(2,2,150,"Green",["Street"])
    reserv1=Reserv(0,[guest1,guest2],room1,datetime(2020,12,11),datetime(2020,12,16))
    guest1.add_reserv(reserv1)
    guest2.add_reserv(reserv1)
    Funct.add_guest(guest1)
    Funct.add_guest(guest2)
    Funct.add_room(room1)
    Funct.add_room(room2)
    Funct.add_reservs(reserv1)
    Funct.show_reservs()
    print()
    Funct.make_reserv([guest1,guest2],1,datetime(2020,12,7),datetime(2020,12,9))
    #Funct.del_reserv(0)
    Funct.make_reserv([guest2], 2, datetime(2020, 12, 9), datetime(2020, 12, 11))
    Funct.show_reservs()
    Funct.show_guests()
    '''Funct.show_guests()
    Funct.show_reserv_guests()
    '''
main()