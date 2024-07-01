from pp_gen import *
# from reduction_tree_comp_42 import *
# from reduction_tree_rachana import *

from PE_defs import *

# ****************** Exact PE ****************** #

def PE_exact(ip,wt):
# def PE_exact(en,ip,wt,opfb):    
# if en==1:
    pp_res=pp_gen(ip,wt)
    #print("PP_RES = ",pp_res)  
    opres=pp_reduction_exact(pp_res)
    if ip == -128 and wt == -128:
        opres=opres*-1
    op = opres
        # op = opres+opfb
    #     Nip=ip
    # else :
    #     Nip=0
    #     # op=opfb


    # return [Nip,op]
    return op

# ********************** PE Approx ********************* #

def PE_approx(ip,wt,pos):
# def PE_approx(en,ip,wt,opfb,pos):
# if en==1:
    pp_res=pp_gen(ip,wt)
    # opres=select_multiplier(pp_res,pos)
    opres=PE_Approx_42(pp_res,pos)
    if ip == -128 and wt == -128:
        opres=opres*-1
    op = opres
        # op = opres+opfb
    #     Nip=ip
    # else :
    #     Nip=0
    #     op=opfb
   
    return op
    # return [Nip,op] 

# # for i in range(-128,127):
# #     for j in range(-128,127):
# #         PE(1,i,j,0)