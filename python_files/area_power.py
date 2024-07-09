def power_45nm(position):
    n=len(position)
    # initial power of 16exact42,9FA,8exact52,1HA,16FA,2pos4 compressors
    power=5.82

    for i in range(n):
    
        if position[i]==1:
            #Approx_52_42_1
            power=power+0.11775

        elif position[i]==2:
            #Approx_52_42_2
            power=power+0.123092
        elif position[i]==3:
            #Approx_42_1
            power=power+0.0482863
        elif position[i]==4:
            #Approx_42_2
            power=power+0.03992
        elif position[i]==5:
            #Approx_42_3
            power=power+0.205181
        elif position[i]==6:
            #Approx_42_4
            power=power+0.205181
        elif position[i]==7:
            #Approx_42_5
            power=power+0.173251
        elif position[i]==8:
            #Approx_42_6
            power=power+0.127609
        elif position[i]==9:
            #Approx_42_7
            power=power+0.0947361
        
    return power

def area_45nm(position):
    n=len(position)
    
    # initial area of 16exact42,9FA,8exact52,1HA,16FA,2pos4 compressors
    area=428.868
    for i in range(n):
        if position[i]==1:
            #Approx_52_42_1
            area=area+10.26

        elif position[i]==2:
            #Approx_52_42_2
            area=area+8.208

        elif position[i]==3:
            #Approx_42_1
            area=area+6.156

        elif position[i]==4:
            #Approx_42_2
            area=area+4.788

        elif position[i]==5:
            #Approx_42_3
            area=area+15.39

        elif position[i]==6:
            #Approx_42_4
            area=area+15.39

        elif position[i]==7:
            #Approx_42_5
            area=area+13.68

        elif position[i]==8:
            #Approx_42_6
            area=area+10.26

        elif position[i]==9:
            #Approx_42_7
            area=area+9.918


    return area

# FA	5.13	6.40E-02
# HA	3.762	4.83E-02
# exact 4_2	10.26	1.41E-01
# pos1	10.26	1.18E-01
# pos2	8.208	1.23E-01
# pos3	6.156	4.83E-02
# pos4	4.788	3.99E-02
# pos5	15.39	2.05E-01
# pos6	15.39	2.05E-01
# pos7	13.68	1.73E-01
# pos8	10.26	1.28E-01
# pos9	9.918	9.47E-02