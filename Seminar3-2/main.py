def bigSum(num1,num2):
    rez=""
    trecere=0
    for i in range(1,min(len(num1),len(num2))+1):
        s=int(num1[-i])+int(num2[-i])+trecere
        if s>9:
            trecere=1
        else:
            trecere=0
        rez=str(s%10)+rez
    if len(num1)>len(num2):
        for i in range(min(len(num1),len(num2))+1,len(num1)+1):
            s=int(num1[-i])+trecere
            if(s>9):
                trecere=1
            else:
                trecere=0
            rez=str(s%10)+rez
    #if(len(num2)) #analog ^
        '''
        
        
        '''
    if(trecere):
        rez=str(trecere)+rez
    return rez





def main():
    a="999911"
    b="111"
    print(bigSum(a,b))

main()