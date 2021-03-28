def sumapartiala(arr,n):
    if arr.count(n/2)>=2:
        return True
    for i in arr:
        if n-i in arr and n-i != i:
            return True
    return False

def sumaPartiala(lista, a):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i] + lista[j] == a:
                return True
    return False

def main():
    l=[1,1,2,4,10]
    a=6
    print(sumaPartiala(l,a))


main()