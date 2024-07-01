import random
from convolution import *
from area_power import *
import itertools
import pandas as pd

# # Define the S(SSIM) A(AREA) P(POWER) fitness function
# def fitness_SAP_45nm(inputimage,kernal1,kernal2,pos,exactop):

#     # pos=[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26]
#     print(pos)
#     [approxop]=conv_3x3_sobel_approx(inputimage,kernal1,kernal2,pos)
    
#     ssim = metrics.structural_similarity(exactop, approxop, data_range=1.0)
#     # area=area_45nm(pos)
#     # power=power_45nm(pos)

#     # fitness = (1-ssim)*area*power
#     # print("\n        Fitness : ",fitness)
#     print("            SSIM : ",ssim)
#     # print("            Area : ",area)
#     # print("            Power : ",power)
    
#     return ssim



inputimage = imread('cameraman.png')
inputimage = (inputimage/2).astype(int)

kernal1 = np.array([[-32, 0, 32],[-64,  0, 64],[-32, 0, 32]])
kernal2 = np.array([[-32, -64, -32],[0,  0, 0],[32, 64, 32]])

[exactop]=conv_3x3_sobel_exact(inputimage,kernal1,kernal2)
print("exacttop done")

# Generate all combinations of the ranges
combinations = itertools.product(range(1, 5), repeat=6)

# Create lists to store the combinations, SSIM values, and multipliers
data = []
SSIM = []
multiplier = []
AreaPowerProd = []
# Initialize count
count = 1



# Print each combination
for combo in combinations:
    i, j, k, l, m, n = combo
    # print(f"i = {i}, j = {j}, k = {k}, l = {l}")
    # pos = [i, j, k, l, m, n]
    pos = [1,4,5,6,2,3]
    print(pos)
    [approxop]=conv_3x3_sobel_approx(inputimage,kernal1,kernal2,pos)
    ssim = metrics.structural_similarity(exactop, approxop, data_range=1.0)
    mul = "mul" + str(count)

    # Hardware parameters extrapolation
    area=area_45nm(pos)
    power=power_45nm(pos)

    # appending the values to their respective list
    data.append(pos)
    SSIM.append(ssim)
    multiplier.append(mul)
    AreaPowerProd.append(area*power)

    count += 1    
    print("            SSIM : ",ssim)

# Convert the list to a DataFrame
df = pd.DataFrame({
    'Multiplier': multiplier,
    'position': data,
    'SSIM': SSIM,
    'Cost function' : AreaPowerProd
})

# Write the DataFrame to an Excel file
df.to_excel('combinations.xlsx', index=False)

# Write the DataFrame to an CSV for dataset 
df.to_csv('output.csv', index=False)


