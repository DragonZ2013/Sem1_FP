def isprim (val):
    if(val<2):
        return False
    if(val==2):
        return True
    if(val%2==0):
        return False
    i=3
    while i*i<=val:
        if(val%i==0):
            return False
        i=i+2
    return True



def a1 (val):

    if val>=0:
        print("2")
    nr=3
    i=1
    while i<val:
        if(isprim(nr)):
            print(str(nr)+" ")
            i+=1
        nr+=2


n= int(input("n="))
a1(n)


