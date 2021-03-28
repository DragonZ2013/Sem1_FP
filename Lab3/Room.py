class Room:
    def __init__(self, nr, maxguest, price,color,view=[]):
        self.__nr=nr
        self.__maxguest=maxguest
        self.__price=price
        self.__color=color
        self.__view=view
    @property
    def nr(self): return self.__nr
    @property
    def maxguest(self): return self.__maxguest
    @property
    def price(self): return self.__price
    @property
    def color(self): return self.__color
    @property
    def view(self): return self.__view
    @nr.setter
    def nr(self,a): self.__nr = a
    @maxguest.setter
    def maxguest(self,a): self.__maxguest = a
    @price.setter
    def price(self, a): self.__price = a
    @color.setter
    def color(self,a): self.__color = a
    @view.setter
    def view(self,a): self.__view = a

    def __str__(self):
        return "Nr:"+str(self.__nr)+" MaxGuests:"+str(self.__maxguest)+" "+str(self.__price)+" "+str(self.__color)+" "+str(self.__view)

    def change_cost(self,price):
        self.price=price
    def isfilter(self,price,view):
        if(self.__price>price):
            return False
        if(view != "" and view not in self.__view):
            return False
        return True