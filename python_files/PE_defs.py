from compressors_rachana import *
from pp_gen import *
from reduction_tree import *

# ******************** Reduction Module Exact ********************** #

def pp_reduction_exact(pp):

    pp1 = [0 for j in range(16)]
    pp2 = [0 for j in range(17)]
    
    # ********* first stage *********#
    
    cin1 = [0 for j in range(17)]
    cin2 = [0 for j in range(17)]
    pp_1st_stage = [[0 for i in range(17)] for j in range(4)]

    for i in range(16):
        [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i],cin1[i+1],cin2[i+1]]=exact_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]],cin1[i],cin2[i])

    # ********* second stage *********#
   
    cin21 = [0 for j in range(17)]

    for i in range(16):
        [pp1[i],pp2[i+1],cin21[i+1]]=exact_42(pp_1st_stage[0][i],pp_1st_stage[1][i],pp_1st_stage[2][i],pp_1st_stage[3][i],cin21[i])


    [dpp1,dpp2,dppres]=B2Dconversion(pp1,pp2)

    return dppres



# ************************PE_Approx_42************************

def PE_Approx_42(pp,pos):

    pp1 = [0 for j in range(16)]
    pp2 = [0 for j in range(17)]
    
    # ********* first stage *********#
    
    cin1 = [0 for j in range(17)]
    cin2 = [0 for j in range(17)]
    pp_1st_stage = [[0 for i in range(17)] for j in range(4)]

    for i in range(16):
        if i >=8:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i],cin1[i+1],cin2[i+1]]=exact_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]],cin1[i],cin2[i])
        elif i==7:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1]]=compressors_42(pp[0][i],pp[1][i],pp[2][i],pp[3][i],pos[0])
            [pp_1st_stage[0][i],pp_1st_stage[1][i+1]]=compressors_42(pp[4][i],pp[5][i],pp[6][i],pp[7][i],pos[1])
        elif i==6:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1]]=compressors_42(pp[0][i],pp[1][i],pp[2][i],pp[3][i],pos[2])
            [pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=FA(pp[4][i],pp[5][i],pp[6][i])
        elif i==5:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1]]=compressors_42(pp[0][i],pp[1][i],pp[2][i],pp[3][i],pos[3])
            [pp_1st_stage[0][i],pp_1st_stage[1][i+1]]=HA(pp[4][i],pp[5][i])
        elif i==4:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1]]=compressors_42(pp[0][i],pp[1][i],pp[2][i],pp[3][i],4)
            pp_1st_stage[0][i]= pp[3][i]           
        elif i==3:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1]]=compressors_42(pp[0][i],pp[1][i],pp[2][i],pp[3][i],4)
        elif i==2:
            [pp_1st_stage[2][i+1],pp_1st_stage[3][i]]= [0,0]
            # [pp_1st_stage[2][i+1],pp_1st_stage[3][i]]=FA(pp[0][i],pp[1][i],pp[2][i])
        elif i==1:
            [pp_1st_stage[2][i+1],pp_1st_stage[3][i]]= [0,0]
            # [pp_1st_stage[3][i],pp_1st_stage[2][i+1]] = HA(pp[0][i],pp[1][i])
        elif i==0:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=[pp[0][i],0,0,0]
    # print("pp_1st_stage = ",pp_1st_stage)

       
    # ********* second stage *********#
   
    cin21 = [0 for j in range(17)]


    for i in range(16):
        if i>=6:
            [pp1[i],pp2[i+1],cin21[i+1]]=exact_42(pp_1st_stage[0][i],pp_1st_stage[1][i],pp_1st_stage[2][i],pp_1st_stage[3][i],cin21[i])
        # elif i==7:
        #     [pp1[i],pp2[i+1]]=compressors_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i],pos[6])
        # elif i==6:
        #     [pp1[i],pp2[i+1]]=compressors_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i],pos[7])
        elif i==5 or i==4:
            [pp2[i+1],pp1[i]]=FA(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[0][i])
        elif i==3 or i==2:
            [pp1[i],pp2[i+1]]=HA(pp_1st_stage[3][i],pp_1st_stage[2][i])
        elif i==1 or i==0:
            [pp1[i],pp2[i+1]]=[pp_1st_stage[3][i],0]
    [dpp1,dpp2,dppres]=B2Dconversion(pp1,pp2)
    # print("approx_op in reduction tree",dppres)
    return dppres

# *************************test**********************************************************

# ************************PE_Approx_42************************

def PE_Approx_test(pp,pos):

    pp1 = [0 for j in range(16)]
    pp2 = [0 for j in range(17)]
    
    # ********* first stage *********#
    
    cin1 = [0 for j in range(17)]
    cin2 = [0 for j in range(17)]
    pp_1st_stage = [[0 for i in range(17)] for j in range(4)]

    for i in range(16):
        if i >=8:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i],cin1[i+1],cin2[i+1]]=exact_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]],cin1[i],cin2[i])
        elif i==7:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1]]=compressors_42(pp[0][i],pp[1][i],pp[2][i],pp[3][i],pos[0])
            [pp_1st_stage[0][i],pp_1st_stage[1][i+1]]=compressors_42(pp[4][i],pp[5][i],pp[6][i],pp[7][i],pos[1])
        elif i==6:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1]]=compressors_42(pp[0][i],pp[1][i],pp[2][i],pp[3][i],pos[2])
            [pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=FA(pp[4][i],pp[5][i],pp[6][i])
        elif i==5:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1]]=compressors_42(pp[0][i],pp[1][i],pp[2][i],pp[3][i],pos[3])
            [pp_1st_stage[0][i],pp_1st_stage[1][i+1]]=HA(pp[4][i],pp[5][i])
        elif i==4:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1]]=FA(pp[0][i],pp[1][i],pp[2][i])
            pp_1st_stage[0][i]= pp[3][i]           
        elif i==3:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1]]=FA(pp[0][i],pp[1][i],pp[2][i])
        elif i==2:
            # [pp_1st_stage[2][i+1],pp_1st_stage[3][i]]= [0,0]
            [pp_1st_stage[2][i+1],pp_1st_stage[3][i]]=FA(pp[0][i],pp[1][i],pp[2][i])
        elif i==1:
            # [pp_1st_stage[2][i+1],pp_1st_stage[3][i]]= [0,0]
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1]] = HA(pp[0][i],pp[1][i])
        elif i==0:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=[pp[0][i],0,0,0]
    # print("pp_1st_stage = ",pp_1st_stage)

       
    # ********* second stage *********#
   
    cin21 = [0 for j in range(17)]


    for i in range(16):
        if i>=6:
            [pp1[i],pp2[i+1],cin21[i+1]]=exact_42(pp_1st_stage[0][i],pp_1st_stage[1][i],pp_1st_stage[2][i],pp_1st_stage[3][i],cin21[i])
        # elif i==7:
        #     [pp1[i],pp2[i+1]]=compressors_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i],pos[6])
        # elif i==6:
        #     [pp1[i],pp2[i+1]]=compressors_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i],pos[7])
        elif i==5 or i==4:
            [pp2[i+1],pp1[i]]=FA(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[0][i])
        elif i==3 or i==2:
            [pp1[i],pp2[i+1]]=HA(pp_1st_stage[3][i],pp_1st_stage[2][i])
        elif i==1 or i==0:
            [pp1[i],pp2[i+1]]=[pp_1st_stage[3][i],0]
    [dpp1,dpp2,dppres]=B2Dconversion(pp1,pp2)
    # print("approx_op in reduction tree",dppres)
    return dppres
