def gen_mat(n):
    #0-(n*n-1)
    ''' n=4
    3 2 1 0
    7 6 5 4
    11 10 9 8
    15 14 13 12
    n=5
    4 3 2 1 0
    9 8 7 6 5
    14 13 12 11 10
    19 18 17 16 15
    24 23 22 21 20
    '''
    l=[]
    for i in range(0,n):
        lc=[]
        for j in range(0,n):
            lc.append(i*n+n-1-j)
        l.append(lc)
    return l

def b(n,mat):
    for i in range(0,int(n/2)):
        for j in range(0+i, n-i):
            print(mat[i][j],end =" ")
        for j in range(1+i, n-i):
            print(mat[j][n - 1-i],end =" ")
        for j in range(n - 2-i, -1+i, -1):
            print(mat[n - 1-i][j],end =" ")
        for j in range(n - 2-i, 0+i, -1):
            print(mat[j][i],end =" ")
    if n%2 == 1:
        print(mat[n//2][n//2],end =" ")

    '''
    for i in range(0,n):
        print(mat[0][i])
    for i in range(1,n):
        print(mat[i][n-1])
    for i in range(n-2,-1,-1):
        print(mat[n-1][i])
    for i in range(n-2,0,-1):
        print(mat[i][0])'''


def main():
    n=int(input("n="))
    mat=gen_mat(n)
    for el in mat:
        print(el)
    b(n,mat)





main()