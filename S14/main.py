def first_missing_lin(list):
    for i in range(len(list)):
        if i != list[i]:
            return i
    return list[-1]+1


def first_missing(list,st,dr):
    mij=(st+dr)//2
    if dr<st:
        return st
    if mij==list[mij]:
        return first_missing(list,mij+1,dr)
    else:
        return first_missing(list,st,mij-1)


def find_max(list,st,dr):
    mij = (st+dr)//2
    if st >= dr:
        # print (list[st])
        return list[st]
    return max(find_max(list,st,mij),find_max(list,mij+1,dr))


def main():
    l = [0, 1, 2, 3, 10, 5, 6, 7, 8, 9]
    # print(first_missing(l,0,len(l)-1))
    print(find_max(l , 0 , len(l)-1))


main()