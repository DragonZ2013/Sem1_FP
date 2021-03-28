



class AwesomeSorter:

    def __init__(self, data):

        self.data = data #eine Liste

    def sort(self, data):
        ok=True
        while(ok):
            ok=False
            for i in range(len(data)-1):
                if data[i]>data[i+1]:
                    data[i],data[i+1]=data[i+1],data[i]
                    ok=True


    #hier is where the magic happens

    #Nehmen Sie an, dass die Methode richtig implementiert wurde und die gibt die korrekt sortierte Liste zurück.

        return data


class Sorter(AwesomeSorter):
    def __init__(self,data, filename):
        AwesomeSorter.__init__(self,data)
        self.filename=filename

    def Sorter_Print(self):
        f = open(self.filename,"w")
        f.write(str(self.sort(self.data)))
        print(self.sort(self.data))
        f.close()

def main():
    a = Sorter([5,4,3,2,1],"test.txt")
    a.Sorter_Print()
    b=[5,4,3,2,1]
    a.sort(b)

main()