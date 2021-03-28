class A:
    def __init__(self):
        self.calcI(30)
        print("i from A is", self.i)

    def calcI(self,i):
        self.i=2*i

class B(A):
    def __init__(self):
        super().__init__()

    def calcI(self,i):
        self.i = 3*i

b=B()
stri="abc2"
for x in stri:
    print (x.isalpha())