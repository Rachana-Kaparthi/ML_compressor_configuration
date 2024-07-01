def FA(a,b,c):
    sum = a^b^c
    carry = (a & b) | (b & c) | (c & a)

    return [carry,sum]
def HA(a,b):
    sum = a^b
    carry = a&b

    return [sum,carry]

def exact_42(a,b,c,d,cin):
    [cout,sum1]=FA(d,c,b)
    [carry,sum]=FA(a,cin,sum1)

    return [sum,carry,cout]

def exact_52(a,b,c,d,e,cin1,cin2):
    [cout1,sum1]=FA(d,c,e)
    [cout2,sum2]=FA(b,cin1,sum1)
    [carry,sum]=FA(a,cin2,sum2)

    return [sum,carry,cout1,cout2]

def pos_52(a,b,c,d,e):
    sum = a|b|c|d|e
    carry = (a & (b|c|d|e)) | ((b|c) & (d|e)) | (d&e)

    return [sum,carry]

#chatgpt
def pos1_52(a, b, c, d, e):
    sum = a ^ b ^ c ^ d ^ e
    carry = (a & b) | (c & (a ^ b)) | (d & (a | b)) | (e & (a | b | c))
    
    return [sum,carry]

# chatgpt
def neg1_52(a, b, c, d, e):
    sum_out = a ^ b ^ c ^ d ^ e
    carry_out = (a & b) | (c & (a ^ b)) | (d & (c ^ (a & b))) | (e & (c ^ (a & b)) & (d ^ (c & (a ^ b))))
    return [sum_out, carry_out]

def neg_52(a,b,c,d,e):
    sum = a|b|c|d|e
    carry = (a & (b|c|d|e)) | ((b&c) & (d|e)) | ((d&e) & (b|c))

    return [sum,carry]

# chatgpt
def brent_kung_52(a, b, c, d, e):
    sum_out = a ^ b ^ c ^ d ^ e
    p1 = a & b
    p2 = c & d
    g1 = a | b
    g2 = c | d
    carry_out = (p1 | (p2 & g1)) | (e & (g1 | (p2 & g2)))
    return [sum_out, carry_out]
#own compressor
def comp2_52(a,b,c,d,e):
    sum = ((a ^ b ^ c ^ d ^ e)|(a & (b|c) & (e|d)))
    carry = ((a & (b|c|d|e)) | (b&(c|d|e)) | (c&(d|e)) |(d&e))

    return [sum,carry]

def comp3_52(a,b,c,d,e):
    carry = (a&(b|c|d|e)) | (b&(c|d|e)) | (c&(d|e)) | (e&d)
    sum = a|b|c|d|e

    return [sum,carry]

# https://ijirt.org/master/publishedpaper/IJIRT154363_PAPER.pdf
def comp_52(a,b,c,d,e):
    carry = a|b
    sum = ((a ^ b)&(c & d & e)) | ((~(a ^ b))&(c | d | e))

    return [sum,carry]

def pos_42(a,b,c,d):
    sum = a|b|c|d
    carry = (a&b)|(b&c)|(d&b)|(c&d)

    return [sum,carry]

def neg_42(a,b,c,d):
    sum = a|b|c|d
    carry = (a&b)|(c&d)

    return [sum,carry]

# chatgpt
def neg1_42(a, b, c, d):
    sum_out = a ^ b ^ c ^ d
    carry_out = (a & b) | (c & (a ^ b))
    return [sum_out, carry_out]

# chatgpt
def pos1_42(a, b, c, d):
    sum_out = a ^ b ^ c ^ d
    carry_out = (a & b) | (c & (a ^ b))
    return [sum_out, carry_out]


# Approximate Multiplier Design Using Novel Dual-Stage 4:2 Compressors
def comp1_42(a,b,c,d):
    sum =((a^b)&(c&d))|((~(a^b))&(c|d))
    carry = a|b

    return [sum,carry]

# own compressor

def comp2_42(a,b,c,d):
    sum =((a^b^c^d)|(a & b & c ))
    carry = ((a&b)|(a&c)|(a&d)|(b&c)|(b&d)|(c&d))

    return [sum,carry]

#sir's paper
def approx_pro1_42(a,b,c,d):
    t1 = a^b
    t2 = c^d
    sum = ((~t1)&(t2) | ((t1)&(~t2)) | (a&b&c&d))
    carry = ~((~(a|b)&(~(c&d))) | (~(c|d)&(~(a&b))))
    return [sum,carry]

#sir's paper
def approx_pro2_42(a,b,c,d):
    t1 = a^b
    t2 = c^d
    sum = (~t1)&(t2) | ((t1)&(~t2)) 
    carry = ~((~(a|b)&(~(c&d))) | (~(c|d)&(~(a&b))))
    return [sum,carry]

#sir's paper
def approx_pro3_42(a,b,c,d):
    t1 = a^b
    t2 = c^d
    sum = ((~t1)&(c|d) | (t1)&(~t2)) 
    carry = ~(((~(a|b))&(~(c&d))) | (~(c|d)&(~(a&b))))
    return [sum,carry]

#sir's paper
def approx_pro5_42(a,b,c,d):
    d1 = ~(a|b)
    d2 = ~(c|d)
    d3 = ~(a&b)
    d4 = ~(c&d)
    O4 = d1 & d2
    O3 = (d1 | d2) & (d3 & d4)
    O2 = (d1 | d2) | (d3 & d4)
    carry = ~(O3)                   
    sum = (O3&(~O4)) | (~O2)

    return [sum,carry]

#sir's paper
def approx_pro4_42(a,b,c,d):
    t1 = a^b
    t2 = c^d
    sum = ~((~t1)&(c|d) | (t1)&(~t2))
    carry = ~((~(a|b))&(~(c&d))) | (~(c|d)&(~(a&b)))
    return [sum,carry]

# https://ijirt.org/master/publishedpaper/IJIRT154363_PAPER.pdf
def comp_42(a,b,c,d):
    carry = a|b
    sum = ((a ^ b)&(c & d)) | ((~(a ^ b))&(c | d))

    return [sum,carry]

# https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8605570
#sum = 𝑝1 + 𝑝2 + 𝑝3 + 𝑝4
#  carry = 𝑝1 ∙ (𝑝2 + 𝑝3 + 𝑝4) + 𝑝2 ∙ (𝑝3 + 𝑝4) + 𝑝3 ∙ 𝑝4 
def comp3_42(a,b,c,d):
    carry = (a&(b|c|d)) | (b&(c|d)) | (c&d)
    sum = a|b|c|d

    return [sum,carry]


def compressors_52(a,b,c,d,e,pos):
    if pos==1:
        [sum52,carry52]= pos1_52(a,b,c,d,e)
    elif pos==2:
        [sum52,carry52]= neg1_52(a,b,c,d,e)
    elif pos==3:
        [sum52,carry52]= pos_52(a,b,c,d,e)
    elif pos==4:
        # [sum52,carry52]= brent_kung_52(a,b,c,d,e)
        [sum52,carry52]= neg_52(a,b,c,d,e)
    elif pos==5:
        [sum52,carry52]= brent_kung_52(a,b,c,d,e)
    elif pos==6:
        [sum52,carry52]= pos1_52(a,b,c,d,e)
    elif pos==7:
        [sum52,carry52]= neg1_52(a,b,c,d,e)
    elif pos==8:
        [sum52,carry52]= pos_52(a,b,c,d,e)
    elif pos==9:
        [sum52,carry52]= neg_52(a,b,c,d,e)
    elif pos==10:
        [sum52,carry52]= comp3_52(a,b,c,d,e)        

    return [sum52,carry52]

def compressors_42(a,b,c,d,pos):
    if pos==1:
        [sum42,carry42]= pos1_42(a,b,c,d)
    elif pos==2:
        [sum42,carry42]= comp1_42(a,b,c,d)
    elif pos==3:
        [sum42,carry42]= pos_42(a,b,c,d)
    elif pos==4:
        [sum42,carry42]= neg_42(a,b,c,d)
    elif pos==5:
        [sum42,carry42]= comp2_42(a,b,c,d)
    elif pos==6:
        [sum42,carry42]= approx_pro1_42(a,b,c,d)
    elif pos==7:
        [sum42,carry42]= approx_pro2_42(a,b,c,d)
    elif pos==8:
        [sum42,carry42]= approx_pro3_42(a,b,c,d)
    # elif pos==10:
    #     [sum42,carry42]= comp3_42(a,b,c,d)
    elif pos==9:
        [sum42,carry42]= approx_pro5_42(a,b,c,d)

    return [sum42,carry42]