def interclasare(l1,l2):
    '''
    input:
    l1 = list
    l2 = list
    output:
    return list
    '''
    listrez=[]
    p1=0
    p2=0
    #p3=0
    leng1=len(l1)
    leng2=len(l2)
    while(p1 < leng1 and p2 < leng2):
        if l1[p1]<l2[p2]:
            listrez.append(l1[p1])
            p1+=1
        else:
            listrez.append(l2[p2])
            p2+=1
    '''
    while p1 < leng1:
        listrez.append(l1[p1])
        p1 += 1
    while p2 < leng2:
        listrez.append(l2[p2])
        p2 += 1
    '''
    listrez=listrez+l1[p1:]
    listrez=listrez+l2[p2:]

    return listrez


def sort012(l):
    '''
    input: lista formata din 0,1,2 in orice ordine
    output: lista sortata 0,1,2
    '''
    nrcif=[0,0,0]
    listout=[]
    '''
    for i in range(len(l)):
        nrcif[l[i]]+=1
    '''
    for i in l:
        nrcif[i]+=1
    '''
    for i in range(nrcif[0]):
        listout.append(0)
    for i in range(nrcif[1]):
        listout.append(1)
    for i in range(nrcif[2]):
        listout.append(2)
    '''
    for i in range(nrcif[0]):
        l[i]=0
    for i in range(nrcif[1]):
        l[i+nrcif[0]]=1
    for i in range(nrcif[2]):
        l[i+nrcif[0]+nrcif[1]]=2

    return l

def sortlist(l):
    #l=sorted(l)
    l.sort()


def sumlist(l,nr):
    '''
    input:
    list l lista cu mai mult de 3 elemente
    nr: int suma ceruta

    output: triplet or none
    '''
    '''
    for i in range(0,len(l)):
        #for j in range(i+1,len(l)):
        t=nr-l[i]
        for j in range(i+1,len(l)):
            if t-l[j] in l and t-l[j]!=l[i] and t-l[j]!=l[j]:
                return l[i],l[j],t-l[j]
    '''
    l.sort()
    print(l)
    for i in range(0,len(l)-2):
        t=l[i]
        p1=i+1
        p2=len(l)-1
        while t+l[p1]+l[p2]!=nr and p2>p1:
            if t+l[p1]+l[p2]>nr:
                p2-=1
            else:
                p1+=1
        if p2>p1:
            return t,l[p1],l[p2]


    return None


def count1(l,idx):
    '''
    input: list with numbers
    output: number of 1's
    '''
    if idx==len(l):
        return 0
    if l[idx]==1:
        return 1+count1(l,idx+1)
    else:
        return count1(l,idx+1)

def count1sorted(l,idx,ok):
    '''
    input: list with numbers
    output: number of 1's
    '''
    if ok == True and l[idx]!=1:
        return 0
    if idx==len(l):
        return 0
    if l[idx]==1:
        return 1+count1sorted(l,idx+1,True)
    else:
        return count1sorted(l,idx+1,ok)

def firstnr(l,st,dr,nr):
    mij=(st+dr)//2
    if l[mij]==nr and (mij==0 or l[mij-1]!=nr):
        return mij
    if st>=dr:
        return -1
    if nr>l[mij]:
        return firstnr(l,mij+1,dr,nr)
    else:
        return firstnr(l,st,mij-1,nr)

def lastnr(l,st,dr,nr):
    mij=(st+dr)//2
    if l[mij]==nr and (mij==len(l)-1 or l[mij+1]!=nr):
        return mij
    if st>=dr:
        return -1
    if nr<l[mij]:
        return lastnr(l,st,mij-1,nr)
    else:
        return lastnr(l, mij + 1, dr, nr)


def count1sorted2(l):
    if firstnr(l,0,len(l)-1,1)==-1:
        return 0
    return lastnr(l,0,len(l)-1,1)-firstnr(l,0,len(l)-1,1)+1


def main():
    list1=[0,1,2,7,8,9]
    list2=[1,2,4,5,12]
    #print(interclasare(list1,list2))
    list1=[1,1,1,2,0,1,2,0,0,2,1]
    #print(sort012(list1))
    list1=[1,2,3,7,12,34,11,15]
    #list1=[1,2,3,7,11,12,15,34]

    #print(sumlist(list1,26))
    list1=[241,4,141,4,12,3,14,1,4,1,1,9]
    #print(count1(list1,0))
    list1=[1,1,1,1,1]
    #list1=[0,0,3,4]
    #print(count1sorted(list1,0,False))
    #print(firstnr(list1,0,len(list1)-1,1))
    #print(lastnr(list1,0,len(list1)-1,1))
    print(count1sorted2(list1))
main()