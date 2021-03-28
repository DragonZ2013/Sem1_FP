def Switchvoc(cuv):
    i=0
    j=len(cuv)-1
    l=list(cuv)
    while(i<j):
        if l[i] not in "AEOIUaeiou":
            i+=1
        if l[j] not in "AEOIUaeiou":
            j-=1
        if l[j] in "AEOIUaeiou" and l[i] in "AEOIUaeiou":
            l[j],l[i]=l[i],l[j]
            i+=1
            j-=1
    return "".join(l)


def main():
    stri="Termionator"
    print(Switchvoc(stri))

main()