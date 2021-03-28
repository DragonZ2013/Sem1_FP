def pb1(l):
    n=len(l)
    i=0
    while i<n:
        if l[i] in l[i+1:]:
            l[i:]=l[i+1:]
            n=n-1
            i=i-1
        i=i+1

def pb2(l):
    cont=0
    for i in range(len(l)):
        lf = (l[i]%10)*10+l[i]//10
        if lf in l[i+1:]:
            cont=cont+1
    return cont

def pb3(l):
    copylist=l.copy()
    rez=""
    while(copylist):
        rez=rez+str(max(copylist))
        copylist.remove(max(copylist))
    return rez


def pb4(l): #hash xy.keyxkeyy
    key=l[1]
    rez=[]
    for i in l[1:]:
        rez.append(hash(i+key/100))
    return rez

def pb5(l): #cifrele au paritate diferita
    n=len(l)
    i=0
    while i<n:
        if (l[i]//10)%2 == (l[i]%10)%2:
            l.pop(i)
            n=n-1
            i=i-1
        i=i+1

def pb6(l):
    leng=1
    lengprev=1
    p=0
    pc=0
    for i in range(1,len(l)):
        if l[i-1]%10 == l[i]//10:
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
        print(str(l[i+p])+" ")
        i+=1

def cmmdc(a,b):
    r=a%b
    while r:
        a=b
        b=r
        r=a%b
    return b


def pb7(l,valfrom,valto):
    if valto == valfrom + 1:
        return l[valfrom]
    if valto<valfrom+1:
        return 0
    mul=l[valfrom]*l[valfrom+1]
    divc=cmmdc(l[valfrom],l[valfrom+1])
    mul=mul//divc
    for i in range(valfrom+2,valto):
        divc=cmmdc(mul,l[i])
        mul=(mul*l[i])//divc
    return mul



def main():
    l=[22,44,56,67,22,22,46,65]

    print(pb7(l,0,9))




main()