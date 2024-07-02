from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage import metrics
from wt_st_SA import *
from timeit import default_timer as timer


def conv_3x3_sobel_exact(ipimage,kernal1):

    height=len(ipimage)
    width=len(ipimage[0])
    # print("Exact Sobel - Image Size : ",height," ",width)

    ipimage=[[ipimage[j][i] for i in range(width)]for j in range(height)]

    exact_op_k1=[[0 for i in range(width)] for j in range(height)]

    exact_op=[[0 for i in range(width)] for j in range(height)]

    for i in range(1,height-1):
        for j in range(1,width-1):
            inmat=[ipimage[i+1][j-1:j+2], ipimage[i][j-1:j+2]  ,ipimage[i-1][j-1:j+2]]
            exact_op_k1[i][j]=matrix_mul_exact(inmat,kernal1)
            
    exact_op=np.array(exact_op_k1)

    exact_op1=exact_op.astype('float64')

    max_ap=max(max(x) for x in exact_op1)
    min_ap=min(min(x) for x in exact_op1)
    R2=exact_op1-min_ap
    exact_op=R2/max_ap

    return [exact_op]


def conv_3x3_sobel_approx(ipimage,kernal1,pos):
    
    # pos1=[[pos[0:7],pos[7:14],pos[14:21]],[pos[21:28],pos[28:35],pos[35:42]],[pos[42:49],pos[49:56],pos[56:63]]]
    # pos2=[[pos[63:70],pos[70:77],pos[77:84]],[pos[84:91],pos[91:98],pos[98:105]],[pos[105:112],pos[112:119],pos[119:126]]]
    # print(pos)
    # pos1=[[pos[0],pos[1],pos[2]],[pos[3],pos[4],pos[5]],[pos[6],pos[7],pos[8]]]
    # pos2=[[pos[9],pos[10],pos[11]],[pos[12],pos[13],pos[14]],[pos[15],pos[16],pos[17]]]
  
  
    height=len(ipimage)
    width=len(ipimage[0])
    # print("Approx Sobel - Image Size : ",height," ",width)
 
    ipimage=[[ipimage[j][i] for i in range(width)]for j in range(height)]
  
    approx_op_k1=[[0 for i in range(width)] for j in range(height)]

    approx_op=[[0 for i in range(width)] for j in range(height)]

    for i in range(1,height-1):
        for j in range(1,width-1):
            inmat=[ipimage[i+1][j-1:j+2], ipimage[i][j-1:j+2]  ,ipimage[i-1][j-1:j+2]]
            if(inmat == [[0,0,0],[0,0,0],[0,0,0]]):
                approx_op_k1[i][j] = 0
            else :
                approx_op_k1[i][j] = matrix_mul_approx(inmat,kernal1,pos)
            
            # approx_op_k1[i][j]=(approxop_k1[0][0]+approxop_k1[1][1]+approxop_k1[2][2])/32

    approx_op=np.array(approx_op_k1)

    approx_op1=approx_op.astype('float64')

    max_ap=max(max(x) for x in approx_op1)
    min_ap=min(min(x) for x in approx_op1)
    R2=approx_op1-min_ap
    approx_op=R2/max_ap
                   
    return [approx_op]




