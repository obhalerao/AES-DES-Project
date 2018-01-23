def DES(message,key):
    
    while not len(message)%64==0:
        message+="0"
    k=gensubkeys(key)
    out=""
    
    for i in range(len(message)//64):
        
        out+=des64(message[64*i:64*i+64],k)
    return out

def deDES(message,key):
    
    while not len(message)%64==0:
        message+="0"
    k=gensubkeys(key)
    out=""
    
    for i in range(len(message)//64):
        
        out+=dedes64(message[64*i:64*i+64],k)
    return out
def gensubkeys(key):
    kpa=list(key)
    kplus=[]
    kplus.extend([kpa[56],kpa[48],kpa[40],kpa[32],kpa[24],kpa[16],kpa[8]])
    kplus.extend([kpa[0],kpa[57],kpa[49],kpa[41],kpa[33],kpa[25],kpa[17]])
    kplus.extend([kpa[9],kpa[1],kpa[58],kpa[50],kpa[42],kpa[34],kpa[26]])
    kplus.extend([kpa[18],kpa[10],kpa[2],kpa[59],kpa[51],kpa[43],kpa[35]])
    kplus.extend([kpa[62],kpa[54],kpa[46],kpa[38],kpa[30],kpa[22],kpa[14]])
    kplus.extend([kpa[6],kpa[61],kpa[53],kpa[45],kpa[37],kpa[29],kpa[21]])
    kplus.extend([kpa[13],kpa[5],kpa[60],kpa[52],kpa[44],kpa[36],kpa[28]])
    kplus.extend([kpa[20],kpa[12],kpa[4],kpa[27],kpa[19],kpa[11],kpa[3]])
    c=[]
    d=[]
    for i in range(28):
        c.append(int(kplus[i]))
    for i in range(28):
        d.append(int(kplus[i+28]))

    #print(c)
    #print(d)
    ca=[]
    da=[]    
    ca.append(mls(c,1))
    ca.append(mls(c,2))
    ca.append(mls(c,4))
    ca.append(mls(c,6))
    ca.append(mls(c,8))
    
    ca.append(mls(c,10))
    ca.append(mls(c,12))
    ca.append(mls(c,14))
    ca.append(mls(c,15))
    ca.append(mls(c,1))
    
    ca.append(mls(c,3))
    ca.append(mls(c,5))
    ca.append(mls(c,7))
    ca.append(mls(c,9))
    ca.append(mls(c,11))
    ca.append(mls(c,12))


    da.append(mls(d,1))
    da.append(mls(d,2))
    da.append(mls(d,4))
    da.append(mls(d,6))
    da.append(mls(d,8))
    
    da.append(mls(d,10))
    da.append(mls(d,12))
    da.append(mls(d,14))
    da.append(mls(d,15))
    da.append(mls(d,1))
    
    da.append(mls(d,3))
    da.append(mls(d,5))
    da.append(mls(d,7))
    da.append(mls(d,9))
    da.append(mls(d,11))
    da.append(mls(d,12))
    cda=[]
    #print(ca)
    for i in range(16):
        temp=[]
        temp.extend(ca[i])
        temp.extend(da[i])
        cda.append(temp)
        #print(temp)
    ka=[]
    for i in range(16):
        k=[]
        k.extend([cda[i][13],cda[i][16],cda[i][10],cda[i][23],cda[i][0],cda[i][4]])
        k.extend([cda[i][2],cda[i][27],cda[i][14],cda[i][5],cda[i][20],cda[i][9]])
        k.extend([cda[i][22],cda[i][18],cda[i][11],cda[i][3],cda[i][25],cda[i][7]])
        k.extend([cda[i][15],cda[i][6],cda[i][26],cda[i][19],cda[i][12],cda[i][1]])
        k.extend([cda[i][40],cda[i][51],cda[i][30],cda[i][36],cda[i][46],cda[i][54]])
        k.extend([cda[i][29],cda[i][39],cda[i][50],cda[i][44],cda[i][32],cda[i][47]])
        k.extend([cda[i][43],cda[i][48],cda[i][38],cda[i][55],cda[i][33],cda[i][52]])
        k.extend([cda[i][45],cda[i][42],cda[i][49],cda[i][35],cda[i][28],cda[i][31]])
        ka.append(k)
    
    
    return ka
def mls(a,n):
    temp=a
    for i in range(n):
        temp=ls(temp)
    return temp
def ls(a):
    a2=[]
    a2.extend(a[1:])
    a2.append(a[0])
    return a2
def des64(a,k):
    
    out=""
    m=""
    ip=     [58 ,   50,   42  ,  34,    26 ,  18 ,   10 ,   2,
            60   , 52  , 44   , 36  ,  28  , 20  ,  12  ,  4,
            62,    54   ,46   , 38   , 30  , 22  ,  14  ,  6,
            64 ,   56   ,48   , 40    ,32  , 24  ,  16  ,  8,
            57  ,  49  , 41   , 33    ,25  , 17  ,   9  ,  1,
            59   , 51  , 43   , 35   , 27  , 19  ,  11  ,  3,
            61   , 53  , 45   , 37   , 29  , 21  ,  13  ,  5,
            63   , 55  , 47   , 39   , 31  , 23  ,  15   , 7]
    for i in range(64):
        m+=list(a)[int(ip[i]-1)]
    l=[]
    r=[]
    for i in range(32):
        l.append(int(m[i]))
    for i in range(32):
        r.append(int(m[i+32]))


        
    for i in range (16):
        oldr=r
        f=feistelround(r,k[i])
        for j in range(32):
            r[j]=int(f[j])^l[j]
            l[j]=oldr[j]
    rl=[]
    rl.extend(r)
    rl.extend(l)

    out=""
    fp=     [40,     8,   48,    16,    56,   24,    64,   32,
            39,     7,   47,    15,    55,   23,    63,   31,
            38,     6,   46,    14,    54,   22,    62,   30,
            37,     5,   45,    13,    53,   21,    61,   29,
            36,     4,   44,    12,    52,   20,    60,   28,
            35,     3,   43,    11,    51,   19,    59,   27,
            34,     2,   42,    10,    50,   18,    58,   26,
            33,     1,   41,     9,    49,   17,    57,   25]
    for i in range(64):
        out+=list(a)[int(fp[i]-1)]
    
    return out
def dedes64(a,k): #same as des64 except ip and fp switched and subkey is revered in order
    
    out=""
    m=""
    ip=     [58 ,   50,   42  ,  34,    26 ,  18 ,   10 ,   2,
            60   , 52  , 44   , 36  ,  28  , 20  ,  12  ,  4,
            62,    54   ,46   , 38   , 30  , 22  ,  14  ,  6,
            64 ,   56   ,48   , 40    ,32  , 24  ,  16  ,  8,
            57  ,  49  , 41   , 33    ,25  , 17  ,   9  ,  1,
            59   , 51  , 43   , 35   , 27  , 19  ,  11  ,  3,
            61   , 53  , 45   , 37   , 29  , 21  ,  13  ,  5,
            63   , 55  , 47   , 39   , 31  , 23  ,  15   , 7]
    fp=     [40,     8,   48,    16,    56,   24,    64,   32,
            39,     7,   47,    15,    55,   23,    63,   31,
            38,     6,   46,    14,    54,   22,    62,   30,
            37,     5,   45,    13,    53,   21,    61,   29,
            36,     4,   44,    12,    52,   20,    60,   28,
            35,     3,   43,    11,    51,   19,    59,   27,
            34,     2,   42,    10,    50,   18,    58,   26,
            33,     1,   41,     9,    49,   17,    57,   25]
    for i in range(64):
        m+=list(a)[int(fp[i]-1)]
    l=[]
    r=[]
    for i in range(32):
        l.append(int(m[i]))
    for i in range(32):
        r.append(int(m[i+32]))


        
    for i in reversed(range (16)):
        oldr=r
        f=feistelround(r,k[i])
        for j in range(32):
            r[j]=int(f[j])^l[j]
            l[j]=oldr[j]
    rl=[]
    rl.extend(r)
    rl.extend(l)

    out=""
    
    for i in range(64):
        out+=list(a)[int(ip[i]-1)]
    
    return out
def feistelround(a,subkey):
    return permutation(substitution(keyMixing(expansion(a),subkey)))
def expansion(a):
    e=[]
    for i in range(8):
        e.append(int(a[(4*i-1)%32]))
        e.append(int(a[4*i]))
        e.append(int(a[4*i+1]))
        e.append(int(a[4*i+2]))
        e.append(int(a[4*i+3]))
        e.append(int(a[(4*i+4)%32]))
    return e

def keyMixing(a,subkey):
    m=[]
    for i in range(48):
        m.append(a[i]^subkey[i])
        print
    return m
def substitution(a):
    #print(a)
    stable=[[['1110', '0100', '1101', '0001', '0010', '1111', '1011', '1000', '0011', '1010', '0110', '1100', '0101', '1001', '0000', '0111'], ['0000', '1111', '0111', '0100', '1110', '0010', '1101', '0001', '1010', '0110', '1100', '1011', '1001', '0101', '0011', '1000'], ['0100', '0001', '1110', '1000', '1101', '0110', '0010', '1011', '1111', '1100', '1001', '0111', '0011', '1010', '0101', '0000'], ['1111', '1100', '1000', '0010', '0100', '1001', '0001', '0111', '0101', '1011', '0011', '1110', '1010', '0000', '0110', '1101']], [['1111', '0001', '1000', '1110', '0110', '1011', '0011', '0100', '1001', '0111', '0010', '1101', '1100', '0000', '0101', '1010'], ['0011', '1101', '0100', '0111', '1111', '0010', '1000', '1110', '1100', '0000', '0001', '1010', '0110', '1001', '1011', '0101'], ['0000', '1110', '0111', '1011', '1010', '0100', '1101', '0001', '0101', '1000', '1100', '0110', '1001', '0011', '0010', '1111'], ['1101', '1000', '1010', '0001', '0011', '1111', '0100', '0010', '1011', '0110', '0111', '1100', '0000', '0101', '1110', '1001']], [['1010', '0000', '1001', '1110', '0110', '0011', '1111', '0101', '0001', '1101', '1100', '0111', '1011', '0100', '0010', '1000'], ['1101', '0111', '0000', '1001', '0011', '0100', '0110', '1010', '0010', '1000', '0101', '1110', '1100', '1011', '1111', '0001'], ['1101', '0110', '0100', '1001', '1000', '1111', '0011', '0000', '1011', '0001', '0010', '1100', '0101', '1010', '1110', '0111'], ['0001', '1010', '1101', '0000', '0110', '1001', '1000', '0111', '0100', '1111', '1110', '0011', '1011', '0101', '0010', '1100']], [['0111', '1101', '1110', '0011', '0000', '0110', '1001', '1010', '0001', '0010', '1000', '0101', '1011', '1100', '0100', '1111'], ['1101', '1000', '1011', '0101', '0110', '1111', '0000', '0011', '0100', '0111', '0010', '1100', '0001', '1010', '1110', '1001'], ['1010', '0110', '1001', '0000', '1100', '1011', '0111', '1101', '1111', '0001', '0011', '1110', '0101', '0010', '1000', '0100'], ['0011', '1111', '0000', '0110', '1010', '0001', '1101', '1000', '1001', '0100', '0101', '1011', '1100', '0111', '0010', '1110']], [['0010', '1100', '0100', '0001', '0111', '1010', '1011', '0110', '1000', '0101', '0011', '1111', '1101', '0000', '1110', '1001'], ['1110', '1011', '0010', '1100', '0100', '0111', '1101', '0001', '0101', '0000', '1111', '1010', '0011', '1001', '1000', '0110'], ['0100', '0010', '0001', '1011', '1010', '1101', '0111', '1000', '1111', '1001', '1100', '0101', '0110', '0011', '0000', '1110'], ['1011', '1000', '1100', '0111', '0001', '1110', '0010', '1101', '0110', '1111', '0000', '1001', '1010', '0100', '0101', '0011']], [['1100', '0001', '1010', '1111', '1001', '0010', '0110', '1000', '0000', '1101', '0011', '0100', '1110', '0111', '0101', '1011'], ['1010', '1111', '0100', '0010', '0111', '1100', '1001', '0101', '0110', '0001', '1101', '1110', '0000', '1011', '0011', '1000'], ['1001', '1110', '1111', '0101', '0010', '1000', '1100', '0011', '0111', '0000', '0100', '1010', '0001', '1101', '1011', '0110'], ['0100', '0011', '0010', '1100', '1001', '0101', '1111', '1010', '1011', '1110', '0001', '0111', '0110', '0000', '1000', '1101']], [['0100', '1011', '0010', '1110', '1111', '0000', '1000', '1101', '0011', '1100', '1001', '0111', '0101', '1010', '0110', '0001'], ['1101', '0000', '1011', '0111', '0100', '1001', '0001', '1010', '1110', '0011', '0101', '1100', '0010', '1111', '1000', '0110'], ['0001', '0100', '1011', '1101', '1100', '0011', '0111', '1110', '1010', '1111', '0110', '1000', '0000', '0101', '1001', '0010'], ['0110', '1011', '1101', '1000', '0001', '0100', '1010', '0111', '1001', '0101', '0000', '1111', '1110', '0010', '0011', '1100']], [['1101', '0010', '1000', '0100', '0110', '1111', '1011', '0001', '1010', '1001', '0011', '1110', '0101', '0000', '1100', '0111'], ['0001', '1111', '1101', '1000', '1010', '0011', '0111', '0100', '1100', '0101', '0110', '1011', '0000', '1110', '1001', '0010'], ['0111', '1011', '0100', '0001', '1001', '1100', '1110', '0010', '0000', '0110', '1010', '1101', '1111', '0011', '0101', '1000'], ['0010', '0001', '1110', '0111', '0100', '1010', '1000', '1101', '1111', '1100', '1001', '0000', '0011', '0101', '0110', '1011']]]
    s=[]
    for i in range(8):
        x=2*(a[6*i])+a[6*i+5]
        y=8*a[6*i+1]+4*a[6*i+2]+2*a[6*i+3]+a[6*i+4]
        #print(i)
        #print(x)
        #print(y)
        s.append(stable[i][x][y])
    return s
def permutation (str4):
    f=[]
    temp=""
    for i in str4:
        temp+=str(i)
    a=list(temp)
    f.extend([a[15],a[6],a[19],a[20]])
    f.extend([a[28],a[11],a[27],a[16]])
    f.extend([a[0],a[14],a[22],a[25]])
    f.extend([a[4],a[17],a[30],a[9]])
    f.extend([a[1],a[7],a[23],a[26]])
    f.extend([a[31],a[26],a[2],a[8]])
    f.extend([a[18],a[12],a[29],a[5]])
    f.extend([a[21],a[10],a[3],a[24]])
    
    return f



mess="10001111111110110011110111011001100111101110101000101100110010000001001100110100010101110111100110011011101111001101111111110001"
key="0001001100110100010101110111100110011011101111001101111111110001"
encoded=(DES(mess,key))
print(mess)
print(encoded)
decoded=deDES(encoded,key)
print(decoded)
"""





#this code was used to extract the s table from a text file
with open('DEStable.txt') as f:

    subkeys = []
    sub=[]
    array=[]
    for line in f:
        

        if(len(sub)<4):
            
            
            curr=""
            for c in list(line):
                if(c.isdigit()):
                    curr+=c
                elif not curr=="":
                    curr=(("0000"+(str(bin(int(curr)))[2:])))
                    array.append(curr[-4:])
                    curr=""
            if len(array)>0:
                sub.append(array)
                array=[]
                #print(array)
        #if len(sub)>0:
        else:
            subkeys.append(sub)
            sub=[]
    subkeys.append(sub)
print(subkeys)


The DES Algorithm first generates 16 subkeys from the key.
The message in split into 64 bit chunks and encoded using the feistel algorithm.
The feistel algorithm runs 16 times, once for each subkey.
It has 4 parts expansion,key mixing, substitution, and permutation.

DES was cracked by brute forcing through all of the possible keys.
AES was build from DES, and is much more secure.
"""
