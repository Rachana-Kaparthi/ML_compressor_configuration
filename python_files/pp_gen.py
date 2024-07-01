def findTwoscomplement(str):
    n = len(str)
    i = n - 1
    while(i >= 0):
        if (str[i] == '1'):
            break
        i -= 1
    if (i == -1):
        return '1'+str
    k = i - 1
    str = list(str)
    while(k >= 0):
        if (str[k] == '1'):
            #str = list(str)
            str[k] = '0'
            #str = ''.join(str)
        else:
            #str = list(str)
            str[k] = '1'
            #str = ''.join(str) 
        k -= 1
    str = ''.join(str)    
    return str

def pos_num(A):
    binA='{0:08b}'.format(A,'b')
    #print("binA = ",binA)
    #strA=str(binA)
    #print("strA = ",strA)
    #binA = [*strA]
    #print("binA = ",binA)
    #list_A = [int(i) for i in binA]
    list_A = [int(i) for i in binA]
    #print("list_A = ",list_A)
    return list_A

def neg_num(A):
    A=A*(-1)
    binA='{0:08b}'.format(A,'b')
    #print("binA = ",binA)
    strA=str(binA)
    #print("strA = ",strA)
    compA=findTwoscomplement(strA)
    #print("compA = ",compA)
    binA = [*compA]
    #print("binA = ",binA)
    list_A = [int(i) for i in binA]
    #print("list_A = ",list_A)
    return list_A

def comptwo(A):
    if A<0:
        A=A*(-1)
        binA='{0:08b}'.format(A,'b')
        #print("binA = ",binA)
        strA1=str(binA)
        strA=findTwoscomplement(strA1)
    else :
        binA='{0:08b}'.format(A,'b')
        #print("binA = ",binA)
        strA=str(binA)
        #print("strA = ",strA)
    compA=findTwoscomplement(strA)
    #print("compA = ",compA)
    binA = [*compA]
    #print("binA = ",binA)
    list_A = [int(i) for i in binA]
    #print("list_A = ",list_A)
    return list_A

def pp_gen(A,B):
    if A==-128:
        tmp=B
        B=A
        A=tmp

    if A >=0:
        binA = pos_num(A)
    else:
        binA = neg_num(A)

    if B >=0:
        binB = pos_num(B)
    else:
        binB = neg_num(B)

    #print("binA = ",binA)
    #print("binB = ",binB)
    
    comp2A=comptwo(A)
    #print("comp2AB= ",comp2A)

    binA.reverse()
    binB.reverse()
    comp2A.reverse()
    
    #print("binA rev= ",binA)
    #print("binB rev= ",binB)
    #print("comp2A rev= ",comp2A)


    pp = [[0 for i in range(16)] for j in range(8)]
    # print("before PP = ")
    # for row in pp:
    #     print(row)

    for i in range(8):
        for j in range(16):
            #print(i,",",j)
            if i>j :
                #print("if1")
                pp[i][j]=0
            elif j >= (8+i) :
                #print("if2")
                pp[i][j]=pp[i][j-1]
            elif i==7:
                #print("if3")
                pp[i][j]=comp2A[j-i] & binB[i]
            else:
                #print("if4")
                pp[i][j]=binA[j-i] & binB[i]
    
    #print("PP = ")
    # for row in pp:
    #     print(row)
    
    return pp
 
# pp_gen(-5,-4)


