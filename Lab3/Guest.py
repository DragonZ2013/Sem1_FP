class Guest:
    def __init__(self,id, name, surname, reserv):
        self.__id=id
        self.__name=name
        self.__surname=surname
        self.__reserv=reserv

    @property
    def name(self): return self.__name
    @property
    def surname(self): return self.__surname
    @property
    def reserv(self): return self.__reserv
    @name.setter
    def name(self,a): self__name=a
    @surname.setter
    def surname(self, a): self__surname = a
    @reserv.setter
    def reserv(self, a): self__reserv = a
    def add_reserv(self,reserv):
        self.__reserv.append(reserv)
    def change_name(self,name):
        self.__name=name
    def __str__(self):
        s=str(self.__name)+" "+str(self.__surname)+": "
        for r in self.__reserv:
            s+=str(r)+"; "
        return s