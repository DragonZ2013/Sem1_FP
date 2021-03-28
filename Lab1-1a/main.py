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
    for i in range(1,val):
        if(isprim(i)):
            print(str(i)+" ")


n= int(input("n="))
a1(n)

