def isprim (val):
    '''
    1.Verifica cazurile exceptionale (0,1,2)
    2.Verifica daca numarul este par si diferit de 2
    3.Parcurge numerele impare pana la radical din numarul dat si verifica daca acestea sunt divizibile
    :param val: int
    :return: bool
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
    1.Parcurge numerele de la 1 la n-1 si aplica functia de primalitate (isprim)
    2.In cazul in care isprim=True afiseaza valoarea
    :param val: int
    :return: void
    '''
    for i in range(1,val):
        if(isprim(i)):
            print(str(i)+" ")


def b(arr):
    '''
    1. Parcurge elementele listei incepand cu pozitia 1 si il verifica pe fiecare cu precedentul
    2. Daca 2 elemente consecutive sunt crescatoare creste lungimea curenta (leng)
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
        if arr[i-1] < arr[i]:
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
    n = int(input("n="))
    a1(n)
    n = int(input("numar de elemente="))
    l = []
    for i in range(n):
        l.append(int(input()))
    b(l)

main()