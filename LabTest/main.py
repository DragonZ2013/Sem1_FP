def isPrime(x):
    if x<2:
        return False
    if x==2:
        return True
    if x%2==0:
        return False
    i=3
    while i*i<=x:
        if x%i==0:
            return False
        i+=2
    return True



def fct1():
    file = open("data.txt", "r")
    Lines = file.readlines()
    SumNum = 0
    ContLit = 0
    LinesPrime = 0
    for i in range(len(Lines)):
        x = Lines[i].split(",")
        CLPrime = False
        CLHasVowEnd = False

        for j in x:
            if j.isnumeric():
                if isPrime(int(j)):
                    CLPrime = True
                SumNum += int(j)
            if j.isalpha():
                ContLit+=len(j)
                if j[-1] in "aeoiuAEOIU":
                    CLHasVowEnd=True
        if i%2==1 and CLHasVowEnd == False:
            return "FEHLER"
        if CLPrime:
            LinesPrime += 1
    if isPrime(LinesPrime) == False:
        return "FEHLER"
    if ContLit>SumNum:
        return "FEHLER"
    return "OK"


def main():
    print(fct1())

main()
