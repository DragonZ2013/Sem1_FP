def testfunc(x,y):
    return ((x[0]+y[0]),(x[1]+y[1]))


def main():
    z=testfunc((2,4),(5,6))
    print(z[0],z[1])



main()