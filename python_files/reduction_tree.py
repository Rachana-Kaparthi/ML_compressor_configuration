from compressors_rachana import *
from pp_gen import *

# ************* Single Row Reduction module exact *************** #

def exact_first_stage_single_row_reduction(pp_row,cin1,cin2):
    [sum52,carry52,cout1,cout2]=exact_52(pp_row[3],pp_row[4],pp_row[5],pp_row[6],pp_row[7],cin1,cin2)
    [carry32,sum32]=FA(pp_row[0],pp_row[1],pp_row[2])

    return [sum52,carry52,carry32,sum32,cout1,cout2]

# ************* Single Row Reduction module positive *************** #

def pos_first_stage_single_row_reduction(pp_row):
    [sum52,carry52]=pos_52(pp_row[7],pp_row[6],pp_row[5],pp_row[4],pp_row[3])
    [carry32,sum32]=FA(pp_row[0],pp_row[1],pp_row[2])

    return [sum52,carry52,carry32,sum32]

# ************* Single Row Reduction module negative *************** #

def neg_first_stage_single_row_reduction(pp_row):
    [sum52,carry52]=neg_52(pp_row[7],pp_row[6],pp_row[5],pp_row[4],pp_row[3])
    [carry32,sum32]=FA(pp_row[0],pp_row[1],pp_row[2])

    return [sum52,carry52,carry32,sum32]

# ***************** Binary to decimal conversion ******************* #

def B2Dconversion(pp1,pp2):
    
    res=[0 for i in range(16)]
    carry=[0 for i in range(17)]

    for i in range(16):
        [carry[i+1],res[i]]=FA(pp1[i],pp2[i],carry[i])
    
    pp1.reverse()
    pp2.reverse()
    res.reverse()

    # print("pp1 : ",pp1)
    # print("pp2 : ",pp2[1:17])
    # print("res : ",res)

    spp1 = [str(x) for x in pp1]
    spp2 = [str(x) for x in pp2[1:17]]
    sppres = [str(x) for x in res]
    
    # print("spp1 : ",spp1)
    # print("spp2 : ",spp2)
    # print("sppres : ",sppres)

    jpp1 = int("".join(spp1))
    jpp2 = int("".join(spp2))
    jppres = int("".join(sppres))
    
    # print("jpp1 : ",jpp1)
    # print("jpp2 : ",jpp2)
    # print("jppres : ",jppres)
    
    # sjpp2=jpp2<<1

    # print("sjpp2 : ",sjpp2)
    
    rpp1=str(jpp1)
    rpp2=str(jpp2)
    rppres=str(jppres)
    
    # print("rpp1 : ",rpp1)
    # print("rpp2 : ",rpp2)
    # print("rppres : ",rppres)

    if pp1[0]==1:
        cpp1=findTwoscomplement(rpp1)
        dpp1 = int(cpp1, 2)
        dpp1=dpp1*(-1)
        #print("cpp1 : ",cpp1)
    else :
        cpp1=rpp1
        dpp1 = int(cpp1, 2)
       # print("cpp1 : ",cpp1)
    
    if pp2[1]==1:
        cpp2=findTwoscomplement(rpp2)
        dpp2 = int(cpp2, 2)
        dpp2=dpp2*(-1)
      #  print("cpp2 : ",cpp2)
    else:
        cpp2=rpp2
        dpp2 = int(cpp2, 2)
     #   print("cpp2 : ",cpp2)
    
    if res[0]==1:
        cppres=findTwoscomplement(rppres)
        dppres = int(cppres, 2)
        dppres=dppres*(-1)
      #  print("cpp2 : ",cpp2)
    else:
        cppres=rppres
        dppres = int(cppres, 2)
     #   print("cpp2 : ",cpp2)
    

    # print("decimal pp1 : ", dpp1)
    # print("decimal pp2 : ", dpp2)
    # print("decimal ppres : ", dppres)
    
    return [dpp1,dpp2,dppres]

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


# ********************** Reduction Module PMNI 7-0 (B) *********************** #
def pp_reduction_PMNI_B(pp):

    pp1 = [0 for j in range(16)]
    pp2 = [0 for j in range(17)]
    
    # ********* first stage *********#
    
    cin1 = [0 for j in range(17)]
    cin2 = [0 for j in range(17)]
    pp_1st_stage = [[0 for i in range(17)] for j in range(4)]

    for i in range(16):
        if i >=8:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i],cin1[i+1],cin2[i+1]]=exact_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]],cin1[i],cin2[i])
        else:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=pos_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]])
    # ********* second stage *********#
   
    cin21 = [0 for j in range(17)]

    for i in range(16):
        if i>=8:
            [pp1[i],pp2[i+1],cin21[i+1]]=exact_42(pp_1st_stage[0][i],pp_1st_stage[1][i],pp_1st_stage[2][i],pp_1st_stage[3][i],cin21[i])
        else:
            [pp1[i],pp2[i+1]]=pos_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i])

    [dpp1,dpp2,dppres]=B2Dconversion(pp1,pp2)

    return dppres

# ********************** Reduction Module NMNI 7-0 (B) *********************** #
def pp_reduction_NMNI_B(pp):

    pp1 = [0 for j in range(16)]
    pp2 = [0 for j in range(17)]
    
    # ********* first stage *********#
    
    cin1 = [0 for j in range(17)]
    cin2 = [0 for j in range(17)]
    pp_1st_stage = [[0 for i in range(17)] for j in range(4)]

    for i in range(16):
        if i >=8:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i],cin1[i+1],cin2[i+1]]=exact_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]],cin1[i],cin2[i])
        else:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=neg_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]])
    # ********* second stage *********#
   
    cin21 = [0 for j in range(17)]

    for i in range(16):
        if i>=8:
            [pp1[i],pp2[i+1],cin21[i+1]]=exact_42(pp_1st_stage[0][i],pp_1st_stage[1][i],pp_1st_stage[2][i],pp_1st_stage[3][i],cin21[i])
        else:
            [pp1[i],pp2[i+1]]=neg_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i])

    [dpp1,dpp2,dppres]=B2Dconversion(pp1,pp2)

    return dppres
# ********************** Reduction Module PMSI 7-0 (B) *********************** #
def pp_reduction_PMSI_B(pp):

    pp1 = [0 for j in range(16)]
    pp2 = [0 for j in range(17)]
    
    # ********* first stage *********#
    
    cin1 = [0 for j in range(17)]
    cin2 = [0 for j in range(17)]
    pp_1st_stage = [[0 for i in range(17)] for j in range(4)]

    for i in range(16):
        if i >=8:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i],cin1[i+1],cin2[i+1]]=exact_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]],cin1[i],cin2[i])
        else:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=pos_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]])
    # ********* second stage *********#
   
    cin21 = [0 for j in range(17)]

    for i in range(16):
        if i>=8:
            [pp1[i],pp2[i+1],cin21[i+1]]=exact_42(pp_1st_stage[0][i],pp_1st_stage[1][i],pp_1st_stage[2][i],pp_1st_stage[3][i],cin21[i])
        else:
            [pp1[i],pp2[i+1]]=neg_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i])

    [dpp1,dpp2,dppres]=B2Dconversion(pp1,pp2)

    return dppres
# ********************** Reduction Module NMSI 7-0 (B) *********************** #
def pp_reduction_NMSI_B(pp):

    pp1 = [0 for j in range(16)]
    pp2 = [0 for j in range(17)]
    
    # ********* first stage *********#
    
    cin1 = [0 for j in range(17)]
    cin2 = [0 for j in range(17)]
    pp_1st_stage = [[0 for i in range(17)] for j in range(4)]

    for i in range(16):
        if i >=8:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i],cin1[i+1],cin2[i+1]]=exact_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]],cin1[i],cin2[i])
        else:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=neg_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]])
    # ********* second stage *********#
   
    cin21 = [0 for j in range(17)]

    for i in range(16):
        if i>=8:
            [pp1[i],pp2[i+1],cin21[i+1]]=exact_42(pp_1st_stage[0][i],pp_1st_stage[1][i],pp_1st_stage[2][i],pp_1st_stage[3][i],cin21[i])
        else:
            [pp1[i],pp2[i+1]]=pos_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i])

    [dpp1,dpp2,dppres]=B2Dconversion(pp1,pp2)

    return dppres
# ********************** Reduction Module PMCI 7-0 (B) *********************** #
def pp_reduction_PMCI_B(pp):

    pp1 = [0 for j in range(16)]
    pp2 = [0 for j in range(17)]
    
    # ********* first stage *********#
    
    cin1 = [0 for j in range(17)]
    cin2 = [0 for j in range(17)]
    pp_1st_stage = [[0 for i in range(17)] for j in range(4)]

    for i in range(16):
        if i >=8:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i],cin1[i+1],cin2[i+1]]=exact_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]],cin1[i],cin2[i])
        elif i%2==0:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=pos_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]])
        elif i%2!=0:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=neg_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]])
    # ********* second stage *********#
   
    cin21 = [0 for j in range(17)]

    for i in range(16):
        if i>=8:
            [pp1[i],pp2[i+1],cin21[i+1]]=exact_42(pp_1st_stage[0][i],pp_1st_stage[1][i],pp_1st_stage[2][i],pp_1st_stage[3][i],cin21[i])
        elif i%2==0:
            [pp1[i],pp2[i+1]]=pos_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i])
        elif i%2!=0:
            [pp1[i],pp2[i+1]]=neg_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i])
    
    [dpp1,dpp2,dppres]=B2Dconversion(pp1,pp2)

    return dppres

# ********************** Reduction Module NMCI 7-0 (B) *********************** #
def pp_reduction_NMCI_B(pp):

    pp1 = [0 for j in range(16)]
    pp2 = [0 for j in range(17)]
    
    # ********* first stage *********#
    
    cin1 = [0 for j in range(17)]
    cin2 = [0 for j in range(17)]
    pp_1st_stage = [[0 for i in range(17)] for j in range(4)]

    for i in range(16):
        if i >=8:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i],cin1[i+1],cin2[i+1]]=exact_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]],cin1[i],cin2[i])
        elif i%2==0:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=neg_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]])
        elif i%2!=0:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=pos_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]])
    # ********* second stage *********#
   
    cin21 = [0 for j in range(17)]

    for i in range(16):
        if i>=8:
            [pp1[i],pp2[i+1],cin21[i+1]]=exact_42(pp_1st_stage[0][i],pp_1st_stage[1][i],pp_1st_stage[2][i],pp_1st_stage[3][i],cin21[i])
        elif i%2==0:
            [pp1[i],pp2[i+1]]=neg_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i])
        elif i%2!=0:
            [pp1[i],pp2[i+1]]=pos_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i])
    
    [dpp1,dpp2,dppres]=B2Dconversion(pp1,pp2)

    return dppres

# ********************** Reduction Module PMCSI 7-0 (B) ********************** #
def pp_reduction_PMCSI_B(pp):

    pp1 = [0 for j in range(16)]
    pp2 = [0 for j in range(17)]
    
    # ********* first stage *********#
    
    cin1 = [0 for j in range(17)]
    cin2 = [0 for j in range(17)]
    pp_1st_stage = [[0 for i in range(17)] for j in range(4)]

    for i in range(16):
        if i >=8:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i],cin1[i+1],cin2[i+1]]=exact_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]],cin1[i],cin2[i])
        elif i%2==0:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=pos_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]])
        elif i%2!=0:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=neg_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]])
    # ********* second stage *********#
   
    cin21 = [0 for j in range(17)]

    for i in range(16):
        if i>=8:
            [pp1[i],pp2[i+1],cin21[i+1]]=exact_42(pp_1st_stage[0][i],pp_1st_stage[1][i],pp_1st_stage[2][i],pp_1st_stage[3][i],cin21[i])
        elif i%2==0:
            [pp1[i],pp2[i+1]]=neg_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i])
        elif i%2!=0:
            [pp1[i],pp2[i+1]]=pos_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i])
    
    [dpp1,dpp2,dppres]=B2Dconversion(pp1,pp2)

    return dppres

# ********************** Reduction Module NMCSI 7-0 (B) ********************** #
def pp_reduction_NMCSI_B(pp):

    pp1 = [0 for j in range(16)]
    pp2 = [0 for j in range(17)]
    
    # ********* first stage *********#
    
    cin1 = [0 for j in range(17)]
    cin2 = [0 for j in range(17)]
    pp_1st_stage = [[0 for i in range(17)] for j in range(4)]

    for i in range(16):
        if i >=8:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i],cin1[i+1],cin2[i+1]]=exact_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]],cin1[i],cin2[i])
        elif i%2==0:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=neg_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]])
        elif i%2!=0:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=pos_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]])
    # ********* second stage *********#
   
    cin21 = [0 for j in range(17)]

    for i in range(16):
        if i>=8:
            [pp1[i],pp2[i+1],cin21[i+1]]=exact_42(pp_1st_stage[0][i],pp_1st_stage[1][i],pp_1st_stage[2][i],pp_1st_stage[3][i],cin21[i])
        elif i%2==0:
            [pp1[i],pp2[i+1]]=pos_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i])
        elif i%2!=0:
            [pp1[i],pp2[i+1]]=neg_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i])
    
    [dpp1,dpp2,dppres]=B2Dconversion(pp1,pp2)

    return dppres

# ********************** Reduction Module PMNI 0-7 (N) *********************** #
def pp_reduction_PMNI_N(pp):

    pp1 = [0 for j in range(16)]
    pp2 = [0 for j in range(17)]
    
    # ********* first stage *********#
    
    cin1 = [0 for j in range(17)]
    cin2 = [0 for j in range(17)]
    pp_1st_stage = [[0 for i in range(17)] for j in range(4)]

    for i in range(16):
        if i >=8:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i],cin1[i+1],cin2[i+1]]=exact_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]],cin1[i],cin2[i])
        else:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=pos_first_stage_single_row_reduction([pp[7][i],pp[6][i],pp[5][i],pp[4][i],pp[3][i],pp[2][i],pp[1][i],pp[0][i]])
    # ********* second stage *********#
   
    cin21 = [0 for j in range(17)]

    for i in range(16):
        if i>=8:
            [pp1[i],pp2[i+1],cin21[i+1]]=exact_42(pp_1st_stage[0][i],pp_1st_stage[1][i],pp_1st_stage[2][i],pp_1st_stage[3][i],cin21[i])
        else:
            [pp1[i],pp2[i+1]]=pos_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i])

    [dpp1,dpp2,dppres]=B2Dconversion(pp1,pp2)

    return dppres

# ********************** Reduction Module NMNI 0-7 (N) *********************** #
def pp_reduction_NMNI_N(pp):

    pp1 = [0 for j in range(16)]
    pp2 = [0 for j in range(17)]
    
    # ********* first stage *********#
    
    cin1 = [0 for j in range(17)]
    cin2 = [0 for j in range(17)]
    pp_1st_stage = [[0 for i in range(17)] for j in range(4)]

    for i in range(16):
        if i >=8:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i],cin1[i+1],cin2[i+1]]=exact_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]],cin1[i],cin2[i])
        else:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=neg_first_stage_single_row_reduction([pp[7][i],pp[6][i],pp[5][i],pp[4][i],pp[3][i],pp[2][i],pp[1][i],pp[0][i]])
    # ********* second stage *********#
   
    cin21 = [0 for j in range(17)]

    for i in range(16):
        if i>=8:
            [pp1[i],pp2[i+1],cin21[i+1]]=exact_42(pp_1st_stage[0][i],pp_1st_stage[1][i],pp_1st_stage[2][i],pp_1st_stage[3][i],cin21[i])
        else:
            [pp1[i],pp2[i+1]]=neg_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i])

    [dpp1,dpp2,dppres]=B2Dconversion(pp1,pp2)

    return dppres

# ********************** Reduction Module PMSI 0-7 (N) *********************** #
def pp_reduction_PMSI_N(pp):

    pp1 = [0 for j in range(16)]
    pp2 = [0 for j in range(17)]
    
    # ********* first stage *********#
    
    cin1 = [0 for j in range(17)]
    cin2 = [0 for j in range(17)]
    pp_1st_stage = [[0 for i in range(17)] for j in range(4)]

    for i in range(16):
        if i >=8:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i],cin1[i+1],cin2[i+1]]=exact_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]],cin1[i],cin2[i])
        else:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=pos_first_stage_single_row_reduction([pp[7][i],pp[6][i],pp[5][i],pp[4][i],pp[3][i],pp[2][i],pp[1][i],pp[0][i]])
    # ********* second stage *********#
   
    cin21 = [0 for j in range(17)]

    for i in range(16):
        if i>=8:
            [pp1[i],pp2[i+1],cin21[i+1]]=exact_42(pp_1st_stage[0][i],pp_1st_stage[1][i],pp_1st_stage[2][i],pp_1st_stage[3][i],cin21[i])
        else:
            [pp1[i],pp2[i+1]]=neg_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i])

    [dpp1,dpp2,dppres]=B2Dconversion(pp1,pp2)

    return dppres

# ********************** Reduction Module NMSI 0-7 (N) *********************** #
def pp_reduction_NMSI_N(pp):

    pp1 = [0 for j in range(16)]
    pp2 = [0 for j in range(17)]
    
    # ********* first stage *********#
    
    cin1 = [0 for j in range(17)]
    cin2 = [0 for j in range(17)]
    pp_1st_stage = [[0 for i in range(17)] for j in range(4)]

    for i in range(16):
        if i >=8:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i],cin1[i+1],cin2[i+1]]=exact_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]],cin1[i],cin2[i])
        else:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=neg_first_stage_single_row_reduction([pp[7][i],pp[6][i],pp[5][i],pp[4][i],pp[3][i],pp[2][i],pp[1][i],pp[0][i]])
    # ********* second stage *********#
   
    cin21 = [0 for j in range(17)]

    for i in range(16):
        if i>=8:
            [pp1[i],pp2[i+1],cin21[i+1]]=exact_42(pp_1st_stage[0][i],pp_1st_stage[1][i],pp_1st_stage[2][i],pp_1st_stage[3][i],cin21[i])
        else:
            [pp1[i],pp2[i+1]]=pos_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i])

    [dpp1,dpp2,dppres]=B2Dconversion(pp1,pp2)

    return dppres

# ********************** Reduction Module PMCI 0-7 (N) *********************** #
def pp_reduction_PMCI_N(pp):

    pp1 = [0 for j in range(16)]
    pp2 = [0 for j in range(17)]
    
    # ********* first stage *********#
    
    cin1 = [0 for j in range(17)]
    cin2 = [0 for j in range(17)]
    pp_1st_stage = [[0 for i in range(17)] for j in range(4)]

    for i in range(16):
        if i >=8:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i],cin1[i+1],cin2[i+1]]=exact_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]],cin1[i],cin2[i])
        elif i%2==0:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=pos_first_stage_single_row_reduction([pp[7][i],pp[6][i],pp[5][i],pp[4][i],pp[3][i],pp[2][i],pp[1][i],pp[0][i]])
        elif i%2!=0:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=neg_first_stage_single_row_reduction([pp[7][i],pp[6][i],pp[5][i],pp[4][i],pp[3][i],pp[2][i],pp[1][i],pp[0][i]])
    # ********* second stage *********#
   
    cin21 = [0 for j in range(17)]

    for i in range(16):
        if i>=8:
            [pp1[i],pp2[i+1],cin21[i+1]]=exact_42(pp_1st_stage[0][i],pp_1st_stage[1][i],pp_1st_stage[2][i],pp_1st_stage[3][i],cin21[i])
        elif i%2==0:
            [pp1[i],pp2[i+1]]=pos_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i])
        elif i%2!=0:
            [pp1[i],pp2[i+1]]=neg_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i])
    
    [dpp1,dpp2,dppres]=B2Dconversion(pp1,pp2)

    return dppres

# ********************** Reduction Module NMCI 0-7 (N) *********************** #
def pp_reduction_NMCI_N(pp):

    pp1 = [0 for j in range(16)]
    pp2 = [0 for j in range(17)]
    
    # ********* first stage *********#
    
    cin1 = [0 for j in range(17)]
    cin2 = [0 for j in range(17)]
    pp_1st_stage = [[0 for i in range(17)] for j in range(4)]

    for i in range(16):
        if i >=8:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i],cin1[i+1],cin2[i+1]]=exact_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]],cin1[i],cin2[i])
        elif i%2==0:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=neg_first_stage_single_row_reduction([pp[7][i],pp[6][i],pp[5][i],pp[4][i],pp[3][i],pp[2][i],pp[1][i],pp[0][i]])
        elif i%2!=0:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=pos_first_stage_single_row_reduction([pp[7][i],pp[6][i],pp[5][i],pp[4][i],pp[3][i],pp[2][i],pp[1][i],pp[0][i]])
    # ********* second stage *********#
   
    cin21 = [0 for j in range(17)]

    for i in range(16):
        if i>=8:
            [pp1[i],pp2[i+1],cin21[i+1]]=exact_42(pp_1st_stage[0][i],pp_1st_stage[1][i],pp_1st_stage[2][i],pp_1st_stage[3][i],cin21[i])
        elif i%2==0:
            [pp1[i],pp2[i+1]]=neg_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i])
        elif i%2!=0:
            [pp1[i],pp2[i+1]]=pos_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i])
    
    [dpp1,dpp2,dppres]=B2Dconversion(pp1,pp2)

    return dppres

# ********************** Reduction Module PMCSI 0-7 (N) ********************** #
def pp_reduction_PMCSI_N(pp):

    pp1 = [0 for j in range(16)]
    pp2 = [0 for j in range(17)]
    
    # ********* first stage *********#
    
    cin1 = [0 for j in range(17)]
    cin2 = [0 for j in range(17)]
    pp_1st_stage = [[0 for i in range(17)] for j in range(4)]

    for i in range(16):
        if i >=8:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i],cin1[i+1],cin2[i+1]]=exact_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]],cin1[i],cin2[i])
        elif i%2==0:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=pos_first_stage_single_row_reduction([pp[7][i],pp[6][i],pp[5][i],pp[4][i],pp[3][i],pp[2][i],pp[1][i],pp[0][i]])
        elif i%2!=0:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=neg_first_stage_single_row_reduction([pp[7][i],pp[6][i],pp[5][i],pp[4][i],pp[3][i],pp[2][i],pp[1][i],pp[0][i]])
    # ********* second stage *********#
   
    cin21 = [0 for j in range(17)]

    for i in range(16):
        if i>=8:
            [pp1[i],pp2[i+1],cin21[i+1]]=exact_42(pp_1st_stage[0][i],pp_1st_stage[1][i],pp_1st_stage[2][i],pp_1st_stage[3][i],cin21[i])
        elif i%2==0:
            [pp1[i],pp2[i+1]]=neg_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i])
        elif i%2!=0:
            [pp1[i],pp2[i+1]]=pos_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i])
    
    [dpp1,dpp2,dppres]=B2Dconversion(pp1,pp2)

    return dppres

# ********************** Reduction Module NMCSI 0-7 (N) ********************** #
def pp_reduction_NMCSI_N(pp):

    pp1 = [0 for j in range(16)]
    pp2 = [0 for j in range(17)]
    
    # ********* first stage *********#
    
    cin1 = [0 for j in range(17)]
    cin2 = [0 for j in range(17)]
    pp_1st_stage = [[0 for i in range(17)] for j in range(4)]

    for i in range(16):
        if i >=8:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i],cin1[i+1],cin2[i+1]]=exact_first_stage_single_row_reduction([pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]],cin1[i],cin2[i])
        elif i%2==0:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=neg_first_stage_single_row_reduction([pp[7][i],pp[6][i],pp[5][i],pp[4][i],pp[3][i],pp[2][i],pp[1][i],pp[0][i]])
        elif i%2!=0:
            [pp_1st_stage[3][i],pp_1st_stage[2][i+1],pp_1st_stage[1][i+1],pp_1st_stage[0][i]]=pos_first_stage_single_row_reduction([pp[7][i],pp[6][i],pp[5][i],pp[4][i],pp[3][i],pp[2][i],pp[1][i],pp[0][i]])
    # ********* second stage *********#
   
    cin21 = [0 for j in range(17)]

    for i in range(16):
        if i>=8:
            [pp1[i],pp2[i+1],cin21[i+1]]=exact_42(pp_1st_stage[0][i],pp_1st_stage[1][i],pp_1st_stage[2][i],pp_1st_stage[3][i],cin21[i])
        elif i%2==0:
            [pp1[i],pp2[i+1]]=pos_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i])
        elif i%2!=0:
            [pp1[i],pp2[i+1]]=neg_42(pp_1st_stage[3][i],pp_1st_stage[2][i],pp_1st_stage[1][i],pp_1st_stage[0][i])
    
    [dpp1,dpp2,dppres]=B2Dconversion(pp1,pp2)

    return dppres


# a=-125
# b=-116
# pp_res=pp_gen(a,b)
# print("exact result : ",a*b)
# # print("partial products")
# # for i in range(8):
# #     print(pp_res[i])
# opres=pp_reduction_exact(pp_res)
# opresPMNI=pp_reduction_PMNI_B(pp_res)
# opresNMNI=pp_reduction_NMNI_B(pp_res)
# opresPMSI=pp_reduction_PMSI_B(pp_res)
# opresNMSI=pp_reduction_NMSI_B(pp_res)
# opresPMCI=pp_reduction_PMCI_B(pp_res)
# opresNMCI=pp_reduction_NMCI_B(pp_res)
# opresPMCSI=pp_reduction_PMCSI_B(pp_res)
# opresNMCSI=pp_reduction_NMCSI_B(pp_res)

# opresPMNI1=pp_reduction_PMNI_N(pp_res)
# opresNMNI1=pp_reduction_NMNI_N(pp_res)
# opresPMSI1=pp_reduction_PMSI_N(pp_res)
# opresNMSI1=pp_reduction_NMSI_N(pp_res)
# opresPMCI1=pp_reduction_PMCI_N(pp_res)
# opresNMCI1=pp_reduction_NMCI_N(pp_res)
# opresPMCSI1=pp_reduction_PMCSI_N(pp_res)
# opresNMCSI1=pp_reduction_NMCSI_N(pp_res)

# print("RES = ",opres)
# print("RES PMNI = ",opresPMNI)
# print("RES NMNI = ",opresNMNI)
# print("RES PMNI = ",opresPMSI)
# print("RES NMNI = ",opresNMSI)
# print("RES PMNI = ",opresPMCI)
# print("RES NMNI = ",opresNMCI)
# print("RES PMNI = ",opresPMCSI)
# print("RES NMNI = ",opresNMCSI)

# print("RES PMNI1 = ",opresPMNI1)
# print("RES NMNI1 = ",opresNMNI1)
# print("RES PMNI1 = ",opresPMSI1)
# print("RES NMNI1 = ",opresNMSI1)
# print("RES PMNI1 = ",opresPMCI1)
# print("RES NMNI1 = ",opresNMCI1)
# print("RES PMNI1 = ",opresPMCSI1)
# print("RES NMNI1 = ",opresNMCSI1)

# for i in range(-128,128):
#     for j in range(-128,128):
#         pp_res=pp_gen(i,j)
#         opres=pp_reduction_exact(pp_res)

#         if i*j!=opres:
#             print("ip : ",i," wt : ",j,"op ex : ",i*j,"op calc : ",opres)