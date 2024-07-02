from PE import *
import numpy as np

def matrix_mul_exact(A,B):
    ipA=np.transpose(A)
    C = 0
    for i in range(len(ipA)):
        for j in range(len(B)):
                C += PE_exact(ipA[i][j], B[i][j])
    return C

def matrix_mul_approx(A,B,pos):
    ipA=np.transpose(A)
    C = 0
    for i in range(len(ipA)):
        for j in range(len(B)):
            if(ipA[i][j] == 0 or B[i][j] == 0):
                res = 0
            else:
                res = PE_approx(ipA[i][j], B[i][j], pos)
            C += res
    # C = [[0 for _ in range(3)] for _ in range(3)]
    # for i in range(len(ipA)):
    #     for j in range(len(B[0])):
    #         for k in range(len(B)):
    #             C[i][j] += PE_approx(ipA[i][k], B[k][j], pos)
    return C



# A=np.random.randint(0,15, size=(3,3))
# print("\n \n matrix A :")
# for i in range(3):
#     print(A[i])

# B=np.random.randint(0,15, size=(3,3))
# print("\n \n matrix B :")
# for i in range(3):
#     print(B[i])
# print( "exact",matrix_mul_exact(A,B))
# print( "approx",matrix_mul_approx(A,B,[1,4,5,6,2,3]))

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