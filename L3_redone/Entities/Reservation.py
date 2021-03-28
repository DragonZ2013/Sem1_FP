class Reserv:
    def __init__(self, nr, guests, room, datestart, datefin):
        self.__nr = nr#used as unique ID
        self.__guests = guests
        self.__room = room
        self.__datestart = datestart
        self.__datefin = datefin

    @property#getter nr
    def nr(self): return self.__nr

    @property#getter guests
    def guests(self): return self.__guests

    @property#getter room
    def room(self): return self.__room

    @property#getter datestart
    def datestart(self): return self.__datestart

    @property#getter datefin
    def datefin(self): return self.__datefin

    @nr.setter#setter nr
    def nr(self, a): self.__nr = a

    @guests.setter#setter guests
    def guests(self, a): self.__guests = a

    @room.setter#setter room
    def room(self, a): self.__room = a

    @datestart.setter#setter datestart
    def datestart(self, a): self.__datestart = a

    @datefin.setter#setter datefin
    def datefin(self, a): self.__datefin = a

    def __str__(self):#Reservation string conversion
        return "Reservierungsnummer: " + str(self.__nr) + " Gästeliste: " + str(
            self.__guests) + " Zimmernummer: " + str(self.__room.nr) + " Anfangsdatum: " + str(
            self.__datestart.strftime('%d-%m-%Y')) + " Endtermin: " + str(self.__datefin.strftime('%d-%m-%Y'))

    def __repr__(self):#Reservation representation (used in lists)
        return "ID: " + str(self.__nr)