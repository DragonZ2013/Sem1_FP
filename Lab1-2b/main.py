def primerelativ(val1,val2):
    for i in range(2,min(val1,val2)):
        if val1%i==0 and val2%i==0:
            return False
    return True

def b(arr):
    leng=1
    lengprev=1
    p=0
    pc=0
    for i in range(1,len(arr)):
        if primerelativ(arr[i-1],arr[i]):
            leng=leng+1
        else:
            if(leng>lengprev):
                lengprev=leng
                p=pc
            leng=1
            pc=i
    if (leng > lengprev):
        lengprev = leng
        p = pc
    i=0
    while i<lengprev:
        print(str(arr[i+p])+" ")
        i+=1



n=int(input("numar de elemente="))
l=[]
for i in range(n):
    l.append(int(input()))
b(l)
