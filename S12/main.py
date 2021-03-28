def SumZif(nr):
    '''input: nr: int nr pozitiv
    output: int sum'''
    if nr==0:
        return 0
    else:
        return nr%10+SumZif(nr//10)

def ErsteUpper(str):
    '''input: str: string
    output: str litera'''
    #if str[0]>='A' and str[0]<='Z':
    if str=='':
        return None
    if str[0].isupper():
        return str[0]
    else:
        return ErsteUpper(str[1:])


def ErsteUpper2(str,i):
    '''input: str: string
    i: int position
    output: str litera'''
    #if str[i]>='A' and str[i]<='Z':
    if i==len(str):
        return None

    if str[i].isupper():
        return str[i]

    else:
        return ErsteUpper2(str,i+1)


def NrVoc(str):
    if str=='':
        return 0
    if str[0] in "aeoiuAEOIU":
        return 1+NrVoc(str[1:])
    return NrVoc(str[1:])

def Palindrom(str):
    if len(str)<2:
        return True
    if str[0] == str[-1]:
        return Palindrom(str[1:-1])
    #else:
    #    return False
    return False



def MaxList(liste,i):
    if i == len(liste)-1:
        #print ("*",liste[i])
        return liste[i]
    #print("+",liste[i])
    return max(liste[i],MaxList(liste,i+1))

def MaxList2(liste,i):
    if i == len(liste)-1:
        return liste[i]
    temp=MaxList(liste,i+1)
    if liste[i]>temp:
        return liste[i]
    else:
        return temp

def MaxList3(liste):
    if len(liste)==1:
        return liste[0]
    if liste[0]>liste[1]:
        liste.pop(1)
    else:
        liste.pop(0)
    return MaxList3(liste)

def InListSearch(liste,i,find):
    if len(liste) == i:
        #if isinstance(liste[i], list):
        #    return InListSearch(liste[i], 0, find)
        return False
    if find == liste[i]:
        return True
    if isinstance(liste[i],list):
        if InListSearch(liste[i],0,find):
            return True

    return InListSearch(liste,i+1,find)

def InListSearch2(liste,find):
    for el in liste:
        if isinstance(el,int):
            if find==el:
                return True
        else:
            if InListSearch2(el,find):
                return True
    return False

def SumList(liste):
    if len(liste)==1:
        if isinstance(liste[0], list):
            return SumList(liste[0])
        return liste[0]
    if isinstance(liste[0],list):
        return SumList(liste[0])+SumList(liste[1:])
    return liste[0]+SumList(liste[1:])


#print(SumZif(2564626))
#print(ErsteUpper("aBfagf"))
#print(ErsteUpper2("arfaCdga",0))
#print(NrVoc("Alfeaob"))
#print(Palindrom(""))
#print(MaxList([1,2,3,4,5,6,4,2],0))
#print(MaxList2([1,2,3,4,5,6,4,2],0))
#print(MaxList3([1,2,3,10,5,8,4,2]))
print(InListSearch([[2,1],2,[3]],0,3))
print(InListSearch2([[2,1],2,[3]],3))
#print(SumList([1,[1,2,5,[6]],3,4,5]))