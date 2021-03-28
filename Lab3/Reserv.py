class Reserv:

    def __init__(self,nr, guests, room, datestart, datefin):
        self.__nr=nr
        self.__guests=guests
        self.__room=room
        self.__datestart=datestart
        self.__datefin=datefin

    @property
    def room(self): return self.__room

    @property
    def datestart(self): return self.__datestart

    @property
    def datefin(self): return self.__datefin

    @property
    def nr(self): return self.__nr

    @room.setter
    def room(self, a): self.__room = a

    @datestart.setter
    def datestart(self, a): self.__datestart = a

    @datefin.setter
    def datefin(self, a): self.__datefin = a

    @nr.setter
    def nr(self,a): self.__nr=a

    def __str__(self):
        return str(self.__nr)+" "+str(self.__room.nr)+" "+str(self.__datestart.strftime("%x"))+" "+str(self.__datefin.strftime("%x"))
