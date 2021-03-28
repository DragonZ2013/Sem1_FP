class Raum():
    def __init__(self, name, nr):
        self.__name = name
        self.__nr = nr

    def __eq__(self, other):
        if self.__name == other.__name:
            return True
        return False

    def __str__(self):
        return self.__name+" "+str(self.__nr)
    @property
    def name(self): return self.__name

    @property
    def nr(self): return self.__nr

