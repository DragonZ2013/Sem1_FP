class Pizzeria:
    def __init__(self,name,rating_total,rating_amount,orders):
        self.__name=name
        self.__rating_total=rating_total
        self.__rating_amount=rating_amount
        self.__orders=orders

    @property
    def name(self):
        return self.__name

    @property
    def rating_total(self):
        return self.__rating_total

    @property
    def rating_amount(self):
        return self.__rating_amount

    @property
    def orders(self):
        return self.__orders

    @name.setter
    def name(self, other):
        self.__name = other

    @orders.setter
    def orders(self, other):
        self.__orders = other

    @rating_amount.setter
    def rating_amount(self, other):
        self.__rating_amount = other

    @rating_total.setter
    def rating_total(self, other):
        self.__rating_total = other

    def __str__(self):
        return self.__name+" "+str(self.__rating_total/self.__rating_amount)+" "+str(self.__orders)

    def __repr__(self):
        return self.__name+" "+str(self.__rating_total/self.__rating_amount)+" "+str(self.__orders)


class Client:
    def __init__(self,name,surname,cardNr,orders,favourites):
        self.__name=name
        self.__surname=surname
        self.__cardNr=cardNr
        self.__orders=orders
        self.__favourites = favourites

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def cardNr(self):
        return self.__cardNr

    @property
    def orders(self):
        return self.__orders

    @property
    def favourites(self):
        return self.__favourites

    @name.setter
    def name(self, other):
        self.__name = other

    @surname.setter
    def surname(self, other):
        self.__surname = other

    @favourites.setter
    def favourites(self, other):
        self.__favourites = other

    @cardNr.setter
    def cardNr(self, other):
        self.__cardNr = other

    @orders.setter
    def orders(self, other):
        self.__orders = other

    def __str__(self):
        return self.__name+" "+self.__surname+" "+str(self.__orders)

    def __repr__(self):
        return self.__name+" "+self.__surname+" "+str(self.__orders)

class Funct:
    def __init__(self,PizzeriasList,ClientList):
        self.__Pizzerias=PizzeriasList
        self.__Clients=ClientList


    @property
    def Pizzerias(self):
        return self.__Pizzerias

    @property
    def Clients(self):
        return self.__Clients

    def showPizzerias(self):
        for i in range(0, len(self.__Pizzerias)):
            print(str(i) + " " + str(self.__Pizzerias[i]))

    def showClients(self):
        for i in range(0, len(self.__Clients)):
            print(str(i) + " " + str(self.__Clients[i]))

    def addPizzeira(self, other):
        self.__Pizzerias.append(other)

    def addClient(self, other):
        self.__Clients.append(other)

    def makeOrder(self,idPizza,idClient,Order):
        self.__Pizzerias[idPizza].orders.append(Order)
        self.__Clients[idClient].orders.append(Order)

    def giveRating(self,idPizza,idClient,Rating):
        self.__Pizzerias[idPizza].rating_total+=Rating
        self.__Pizzerias[idPizza].rating_amount+=1
        self.__Clients[idClient].favourites.append([idPizza,Rating])

    def showFavourites(self,idClient):
        print("Favourites of "+self.__Clients[idClient].name+" "+self.__Clients[idClient].surname+":")
        self.__Clients[idClient].favourites.sort(reverse=True,key=lambda x:x[1])
        for i in range(0,min(3,len(self.__Clients[idClient].favourites))):
            print(self.__Pizzerias[self.__Clients[idClient].favourites[i][0]])



def main():
    #name,rating_total,rating_amount,orders
    Pizzeria1 = Pizzeria("Papa Jhon's",9,2,[])
    Pizzeria2 = Pizzeria("Dodo's",14,3,[])
    Pizzeria3 = Pizzeria("Dodo's2",14,3,[])
    Pizzeria4 = Pizzeria("Dodo's3",14,3,[])

    #name,surname,cardNr,orders,favourites
    Client1 = Client("Bob","Dylan",1,[],[])
    Client2 = Client("Dorian","Jebediah",32131,[],[])
    Manage = Funct([Pizzeria1,Pizzeria2,Pizzeria3],[Client1])
    Manage.addPizzeira(Pizzeria4)
    Manage.addClient(Client2)
    Manage.giveRating(0,0,5)
    #Manage.giveRating(1,0,4)
    #Manage.giveRating(2,0,3)
    Manage.giveRating(3,0,2)
    Manage.makeOrder(0,0,"Peperonni")

    Manage.showPizzerias()
    print()
    Manage.showClients()
    print()
    Manage.showFavourites(0)
    print()
    Manage.showFavourites(1)
main()
