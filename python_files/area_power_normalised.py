def power_45nm(position):
    n=len(position)
    power=0
    for i in range(n):
        if position[i]==1:
            #Approx_52_42_1
            power=power+1
        elif position[i]==2:
            #Approx_52_42_2
            power=power+0.968595592
        elif position[i]==3:
            #Approx_42_1
            power=power+0.985472917
        elif position[i]==4:
            #Approx_42_2
            power=power+0.983400263
        elif position[i]==5:
            #Approx_42_3
            power=power+0.853285712
        elif position[i]==6:
            #Approx_42_4
            power=power+0.852434443
        elif position[i]==7:
            #Approx_42_5
            power=power+0.887743583
        elif position[i]==8:
            #Approx_42_6
            power=power+0.85511779
        elif position[i]==9:
            #Approx_42_7
            power=power+0.982863593
        elif position[i]==10:
            #Approx_42_8
            power=power+0.883117123
        elif position[i]==11:
            #Approx_42_9
            power=power+0.850195237
        elif position[i]==12:
            #Approx_42_10
            power=power+0.892036938
        elif position[i]==13:
            #Approx_42_11
            power=power+0.910635305
        elif position[i]==14:
            #Approx_42_12
            power=power+0.932638748
        elif position[i]==15:
            #Approx_42_13
            power=power+0.878453652
        elif position[i]==16:
            #Approx_42_14
            power=power+0.913226123
        elif position[i]==17:
            #PMNI_B
            power=power+0.479800877
        elif position[i]==18:
            #NMNI_B
            power=power+0.423210023
        elif position[i]==19:
            #PMSI_B
            power=power+0.38849307
        elif position[i]==20:
            #NMSI_B
            power=power+0.416048263
        elif position[i]==21:
            #PMCI_B
            power=power+0.440753558
        elif position[i]==22:
            #NMCI_B
            power=power+0.360216148
        elif position[i]==23:
            #PMCSI_B
            power=power+0.439920795
        elif position[i]==24:
            #NMCSI_B
            power=power+0.454688454
        elif position[i]==25:
            #PMNI_N
            power=power+0.058830061
        elif position[i]==26:
            #NMNI_N
            power=power+0.00001
        elif position[i]==27:
            #PMSI_N
            power=power+0.035845809
        elif position[i]==28:
            #NMSI_N
            power=power+0.017821123
        elif position[i]==29:
            #PMCI_N
            power=power+0.023854026
        elif position[i]==30:
            #NMCI_N
            power=power+0.041193997
        elif position[i]==31:
            #PMCSI_N
            power=power+0.044043896
        elif position[i]==32:
            #NMCSI_N
            power=power+0.035068564
                

    return power

def area_45nm(position):
    n=len(position)
    area=0
    for i in range(n):
        if position[i]==1:
            #Approx_52_42_1
            area=area+0.650887574
        elif position[i]==2:
            #Approx_52_42_2
            area=area+0.668639053
        elif position[i]==3:
            #Approx_42_1
            area=area+0.698224852
        elif position[i]==4:
            #Approx_42_2
            area=area+0.653846154
        elif position[i]==5:
            #Approx_42_3
            area=area+0.579881657
        elif position[i]==6:
            #Approx_42_4
            area=area+0.603550296
        elif position[i]==7:
            #Approx_42_5
            area=area+0.653846154
        elif position[i]==8:
            #Approx_42_6
            area=area+0.547337278
        elif position[i]==9:
            #Approx_42_7
            area=area+0.630177515
        elif position[i]==10:
            #Approx_42_8
            area=area+0.615384615
        elif position[i]==11:
            #Approx_42_9
            area=area+0.50295858
        elif position[i]==12:
            #Approx_42_10
            area=area+0.677514793
        elif position[i]==13:
            #Approx_42_11
            area=area+0.633136095
        elif position[i]==14:
            #Approx_42_12
            area=area+0.541420118
        elif position[i]==15:
            #Approx_42_13
            area=area+0.600591716
        elif position[i]==16:
            #Approx_42_14
            area=area+0.600591716
        if position[i]==17:
            #PMNI_B
            area=area+0.99408284
        elif position[i]==18:
            #NMNI_B
            area=area+0.926035503
        elif position[i]==19:
            #PMSI_B
            area=area+0.884615385
        elif position[i]==20:
            #NMSI_B
            area=area+0.955621302
        elif position[i]==21:
            #PMCI_B
            area=area+1
        elif position[i]==22:
            #NMCI_B
            area=area+0.890532544
        elif position[i]==23:
            #PMCSI_B
            area=area+0.934911243
        elif position[i]==24:
            #NMCSI_B
            area=area+0.928994083
        elif position[i]==25:
            #PMNI_N
            area=area+0.065088757
        elif position[i]==26:
            #NMNI_N
            area=area+0.118343195
        elif position[i]==27:
            #PMSI_N
            area=area+0.00001
        elif position[i]==28:
            #NMSI_N
            area=area+0.153846154
        elif position[i]==29:
            #PMCI_N
            area=area+0.079881657
        elif position[i]==30:
            #NMCI_N
            area=area+0.130177515
        elif position[i]==31:
            #PMCSI_N
            area=area+0.112426036
        elif position[i]==32:
            #NMCSI_N
            area=area+0.100591716

    return area