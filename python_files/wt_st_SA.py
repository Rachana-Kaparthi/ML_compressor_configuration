from PE import *
import numpy as np

def matrix_mul_exact(A,B):
    ipA=np.transpose(A)
    C = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(len(ipA)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += PE_exact(ipA[i][k], B[k][j])
    return C

def matrix_mul_approx(A,B,pos):
    ipA=np.transpose(A)
    C = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(len(ipA)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += PE_approx(ipA[i][k], B[k][j], pos)
    return C
 
def wt_st_sa_3x3_exact(matA,matB):
    ipA=np.transpose(matA)
    #matB=np.transpose(matB)
    n=len(matB)
    # ipA=[[0 for i in range(3*n-2)] for j in range(n)]
    op=[[0 for i in range(n)] for j in range(n)]

    #********************* clock 1 ***********************#
    
    # print("\n clock 1")

    #ROW1
    [NA100,op100]=PE_exact(1,ipA[0][0],matB[0][0],0)
    
    #********************* clock 2 ***********************#
    
    # print("\n clock 2")

    #ROW1
    [NA200,op200]=PE_exact(1,ipA[0][1],matB[0][0],0)
    [NA201,op201]=PE_exact(1,NA100,    matB[0][1],0)

    #ROW2
    [NA210,op210]=PE_exact(1,ipA[1][0],matB[1][0],op100)
    
    #********************* clock 3 ***********************#
    
    # print("\n clock 3")

    #ROW1
    [NA300,op300]=PE_exact(1,ipA[0][2],matB[0][0],0)
    [NA301,op301]=PE_exact(1,NA200,    matB[0][1],0)
    [NA302,op302]=PE_exact(1,NA201,    matB[0][2],0)

    #ROW2
    [NA310,op310]=PE_exact(1,ipA[1][1],matB[1][0],op200)
    [NA311,op311]=PE_exact(1,NA210,    matB[1][1],op201)

    #ROW3
    [NA320,op[0][0]]=PE_exact(1,ipA[2][0],matB[2][0],op210)

    #********************* clock 4 ***********************#
    
    # print("\n clock 4")
    
    #ROW1
    [NA401,op401]=PE_exact(1,NA300,    matB[0][1],0)
    [NA402,op402]=PE_exact(1,NA301,    matB[0][2],0)
   
    #ROW2
    [NA410,op410]=PE_exact(1,ipA[1][2],matB[1][0],op300)
    [NA411,op411]=PE_exact(1,NA310,    matB[1][1],op301)
    [NA412,op412]=PE_exact(1,NA311,    matB[1][2],op302)


    #ROW3
    [NA420,op[1][0]]=PE_exact(1,ipA[2][1],matB[2][0],op310)
    [NA421,op[0][1]]=PE_exact(1,NA320,    matB[2][1],op311)

   
    #********************* clock 5 ***********************#
    
    # print("\n clock 5")
    
    #ROW1
    [NA502,op502]=PE_exact(1,NA401,    matB[0][2],0)

    #ROW2
    [NA511,op511]=PE_exact(1,NA410,    matB[1][1],op401)
    [NA512,op512]=PE_exact(1,NA411,    matB[1][2],op402)


    #ROW3
    [NA520,op[2][0]]=PE_exact(1,ipA[2][2],matB[2][0],op410)
    [NA521,op[1][1]]=PE_exact(1,NA420,    matB[2][1],op411)
    [NA522,op[0][2]]=PE_exact(1,NA421,    matB[2][2],op412)

    #********************* clock 6 ***********************#
    
    # print("\n clock 6")
    
    #ROW2
    [NA612,op612]=PE_exact(1,NA511,    matB[1][2],op502)

    #ROW3
    [NA621,op[2][1]]=PE_exact(1,NA520,    matB[2][1],op511)
    [NA622,op[1][2]]=PE_exact(1,NA521,    matB[2][2],op512)

    #********************* clock 7 ***********************#
    
    # print("\n clock 7")
    
    #ROW3
    [NA722,op[2][2]]=PE_exact(1,NA621,    matB[2][2],op612)
        
    return (op)


def wt_st_sa_3x3_approx(matA,matB,pos):
    ipA=np.transpose(matA)
    #matB=np.transpose(matB)
    n=len(matB)
    # ipA=[[0 for i in range(3*n-2)] for j in range(n)]
    op=[[0 for i in range(n)] for j in range(n)]

    #********************* clock 1 ***********************#
    
    # print("\n clock 1")

    #ROW1
    [NA100,op100]=PE_approx(1,ipA[0][0],matB[0][0],0,pos)
    
    #********************* clock 2 ***********************#
    
    # print("\n clock 2")

    #ROW1
    [NA200,op200]=PE_approx(1,ipA[0][1],matB[0][0],0,pos)
    [NA201,op201]=PE_approx(1,NA100,    matB[0][1],0,pos)

    #ROW2
    [NA210,op210]=PE_approx(1,ipA[1][0],matB[1][0],op100,pos)
    
    #********************* clock 3 ***********************#
    
    # print("\n clock 3")

    #ROW1
    [NA300,op300]=PE_approx(1,ipA[0][2],matB[0][0],0,pos)
    [NA301,op301]=PE_approx(1,NA200,    matB[0][1],0,pos)
    [NA302,op302]=PE_approx(1,NA201,    matB[0][2],0,pos)

    #ROW2
    [NA310,op310]=PE_approx(1,ipA[1][1],matB[1][0],op200,pos)
    [NA311,op311]=PE_approx(1,NA210,    matB[1][1],op201,pos)

    #ROW3
    [NA320,op[0][0]]=PE_approx(1,ipA[2][0],matB[2][0],op210,pos)

    #********************* clock 4 ***********************#
    
    # print("\n clock 4")
    
    #ROW1
    [NA401,op401]=PE_approx(1,NA300,    matB[0][1],0,pos)
    [NA402,op402]=PE_approx(1,NA301,    matB[0][2],0,pos)
   
    #ROW2
    [NA410,op410]=PE_approx(1,ipA[1][2],matB[1][0],op300,pos)
    [NA411,op411]=PE_approx(1,NA310,    matB[1][1],op301,pos)
    [NA412,op412]=PE_approx(1,NA311,    matB[1][2],op302,pos)


    #ROW3
    [NA420,op[1][0]]=PE_approx(1,ipA[2][1],matB[2][0],op310,pos)
    [NA421,op[0][1]]=PE_approx(1,NA320,    matB[2][1],op311,pos)

   
    #********************* clock 5 ***********************#
    
    # print("\n clock 5")
    
    #ROW1
    [NA502,op502]=PE_approx(1,NA401,    matB[0][2],0,pos)

    #ROW2
    [NA511,op511]=PE_approx(1,NA410,    matB[1][1],op401,pos)
    [NA512,op512]=PE_approx(1,NA411,    matB[1][2],op402,pos)


    #ROW3
    [NA520,op[2][0]]=PE_approx(1,ipA[2][2],matB[2][0],op410,pos)
    [NA521,op[1][1]]=PE_approx(1,NA420,    matB[2][1],op411,pos)
    [NA522,op[0][2]]=PE_approx(1,NA421,    matB[2][2],op412,pos)

    #********************* clock 6 ***********************#
    
    # print("\n clock 6")
    
    #ROW2
    [NA612,op612]=PE_approx(1,NA511,    matB[1][2],op502,pos)

    #ROW3
    [NA621,op[2][1]]=PE_approx(1,NA520,    matB[2][1],op511,pos)
    [NA622,op[1][2]]=PE_approx(1,NA521,    matB[2][2],op512,pos)

    #********************* clock 7 ***********************#
    
    # print("\n clock 7")
    
    #ROW3
    [NA722,op[2][2]]=PE_approx(1,NA621,    matB[2][2],op612,pos)
        
    return (op)


def enable_PE(n,clk_no):
    count=0
    #print("clk_no : ",clk_no)
    if(clk_no>n):
        matrix = [[0 for i in range(clk_no+1)] for j in range(clk_no+1)]
    else:
        matrix = [[0 for i in range(n)] for j in range(n)]
    zero_rows=0
    noofzeros=0
    if(clk_no>n):
        zero_rows=clk_no-n
        for i in range(1,zero_rows+1):
            noofzeros =noofzeros+i
            #print("noofzeros = ",noofzeros)

    for i in range(1,clk_no+1):
        count =count+i
        #print("count = ",count)

    index=1
    #print("count = ",count)
    if (count==1):
        matrix[0][0]=1

    for i in range(1,clk_no+1):
        #print("i = ",i)
        for j in range(i):
            #print("j = ",j)
            if index > count:
                break
            #print("noofzeros = ",noofzeros)
            if noofzeros>0:    
                matrix[j][i-1-j]=0
                noofzeros=noofzeros-1
            else :   
                matrix[j][i-1-j]=1
                index = index + 1

        if index > count:
            break
    
    return matrix[0:9][0:9]


# matA=np.random.randint(-128,127, size=(3,3))
# print("\n \n matrix A :")
# for i in range(3):
#     print(matA[i])

# matB=np.random.randint(-128,127, size=(3,3))
# print("\n \n matrix B :")
# for i in range(3):
#     print(matB[i])

# # pos=[[7,7,7],[7,7,8],[6,6,6]]
# op_mat=wt_st_sa_3x3_exact(matA,matB)
# print("\n \n Final output matrix :")
# for i in range(3):
#     print(op_mat[i])

# # matrix = [[0 for i in range(3)] for j in range(3)]
# result = np.dot(matA,matB)
# print("\n \n exact output matrix :")
# for i in range(3):
#     print(result[i])

# # if op_mat.all()==result.all():
# #     print("matrices match")