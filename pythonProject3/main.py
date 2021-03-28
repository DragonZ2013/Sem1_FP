def decode(strin):
    strcheck = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    strcheck =list(strcheck)
    pos = 0
    resout = []

    for i in range(0,len(strin)):
        if strin[i]=='+':
            resout.append(strcheck[pos])
            if i<len(strin)-1 and strin[i+1].isdigit():
                for j in range(1,int(strin[i+1])):
                    resout.append(strcheck[pos])
                i=i+1
        if strin[i]=='<':
            pos=pos-1
        if strin[i]=='>':
            pos=pos+1
        if strin[i]=='|':
            strcheck.pop(pos)
        if strin[i]=='$':
            #print(resout+list(resout[len(resout)-1]))
            resout = resout+list(resout[len(resout)-1])


    return ''.join(resout)


print(decode("+>>>+2<<<+$"))