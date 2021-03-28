def isprim (val):
    '''
    1.Verifica cazurile exceptionale (0,1,2)
    2.Verifica daca numarul este par si diferit de 2
    3.Parcurge numerele impare pana la radical din numarul dat si verifica daca acestea sunt divizibile
    :param val: int
    :return: True/False
    '''
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
    '''
    1.Afiseaza 2 (primul numar prim) daca afiseaza cel putin o valoare
    2.Parcurge numele impare de la 3 si daca sunt prime le afiseaza si creste valoare lui i
    3.Functia se termina cand i ajunge la valoarea parametrului dat
    :param val: int
    :return: void
    '''
    if val>=0:
        print("2")
    nr=3
    i=1
    while i<val:
        if(isprim(nr)):
            print(str(nr)+" ")
            i+=1
        nr+=2


def primerelativ(val1,val2):
    '''
    1.Parcurge numerele de la 2 pana la cea mai mica din valorile date
    2.In cazul in care ambele valori sunt divizibile cu aceleasi numar return False
    3.Daca ajunge la finalul repetitivei fara sa returneze False, return True
    :param val1: int
    :param val2: int
    :return: bool
    '''
    for i in range(2,min(val1,val2)+1):
        if val1%i==0 and val2%i==0:
            return False
    return True

def b(arr):
    '''
       1. Parcurge elementele listei incepand cu pozitia 1 si il verifica pe fiecare cu precedentul
       2. Daca 2 elemente consecutive sunt prime intre ele creste lungimea curenta (leng)
       3. In caz contrar, daca lungimea este mai mare decat cea anterioara actualizeaza lungimea maxima (lengprev) si pozitia finala (p)
       4. La iesirea din for verifica daca ultimul subsir respecta conditia data
       5. Afiseaza elementele
       :param arr: list
       :return: void
    '''
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


def main():
    '''n = int(input("n="))
    a1(n)'''
    n = int(input("numar de elemente="))
    l = []
    for i in range(n):
        l.append(int(input()))
    b(l)


main()