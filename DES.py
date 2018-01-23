def DES(message,key):
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
    ca.apend(mls(c,1))
    ca.apend(mls(c,2))
    ca.apend(mls(c,4))
    ca.apend(mls(c,6))
    ca.apend(mls(c,8))
    
    ca.apend(mls(c,10))
    ca.apend(mls(c,12))
    ca.apend(mls(c,14))
    ca.apend(mls(c,15))
    ca.apend(mls(c,1))
    
    ca.apend(mls(c,3))
    ca.apend(mls(c,5))
    ca.apend(mls(c,7))
    ca.apend(mls(c,9))
    ca.apend(mls(c,11))
    ca.apend(mls(c,12))


    da.apend(mls(d,1))
    da.apend(mls(d,2))
    da.apend(mls(d,4))
    da.apend(mls(d,6))
    da.apend(mls(d,8))
    
    da.apend(mls(d,10))
    da.apend(mls(d,12))
    da.apend(mls(d,14))
    da.apend(mls(d,15))
    da.apend(mls(d,1))
    
    da.apend(mls(d,3))
    da.apend(mls(d,5))
    da.apend(mls(d,7))
    da.apend(mls(d,9))
    da.apend(mls(d,11))
    da.apend(mls(d,12))
    return
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
    l=[]
    r=[]
    for i in range(32):
        l.append(a[i])
    for i in range(32):
        r.append(a[i+32])
    
    return
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




key="0001001100110100010101110111100110011011101111001101111111110001"
DES("",key)


s="11110000101010101111000010101010"
a=list(s)
k="000110110000001011101111111111000111000001110010"
sk=[]
print(list(k))
for i in list(k):
    sk.append(int(i))
#print(sk)
f=feistelround(a,sk)
out=""
for i in f:
    out+=i
print(out)
"""
s="011000010001011110111010100001100110010100100111"
a=[]
print(len(s))
for i in list(s):
    a.append(int(i))
print(a)
a=substitution(a)
print(a)
out=""
for i in a:
    out+= str(i)
print(out)



s="11110000101010101111000010101010"
out=""
for i in (expansion(list(s))):
    out+= i
print(out)

stable=[[['1110', '0100', '1101', '0001', '0010', '1111', '1011', '1000', '0011', '1010', '0110', '1100', '0101', '1001', '0000', '0111'], ['0000', '1111', '0111', '0100', '1110', '0010', '1101', '0001', '1010', '0110', '1100', '1011', '1001', '0101', '0011', '1000'], ['0100', '0001', '1110', '1000', '1101', '0110', '0010', '1011', '1111', '1100', '1001', '0111', '0011', '1010', '0101', '0000'], ['1111', '1100', '1000', '0010', '0100', '1001', '0001', '0111', '0101', '1011', '0011', '1110', '1010', '0000', '0110', '1101']], [['1111', '0001', '1000', '1110', '0110', '1011', '0011', '0100', '1001', '0111', '0010', '1101', '1100', '0000', '0101', '1010'], ['0011', '1101', '0100', '0111', '1111', '0010', '1000', '1110', '1100', '0000', '0001', '1010', '0110', '1001', '1011', '0101'], ['0000', '1110', '0111', '1011', '1010', '0100', '1101', '0001', '0101', '1000', '1100', '0110', '1001', '0011', '0010', '1111'], ['1101', '1000', '1010', '0001', '0011', '1111', '0100', '0010', '1011', '0110', '0111', '1100', '0000', '0101', '1110', '1001']], [['1010', '0000', '1001', '1110', '0110', '0011', '1111', '0101', '0001', '1101', '1100', '0111', '1011', '0100', '0010', '1000'], ['1101', '0111', '0000', '1001', '0011', '0100', '0110', '1010', '0010', '1000', '0101', '1110', '1100', '1011', '1111', '0001'], ['1101', '0110', '0100', '1001', '1000', '1111', '0011', '0000', '1011', '0001', '0010', '1100', '0101', '1010', '1110', '0111'], ['0001', '1010', '1101', '0000', '0110', '1001', '1000', '0111', '0100', '1111', '1110', '0011', '1011', '0101', '0010', '1100']], [['0111', '1101', '1110', '0011', '0000', '0110', '1001', '1010', '0001', '0010', '1000', '0101', '1011', '1100', '0100', '1111'], ['1101', '1000', '1011', '0101', '0110', '1111', '0000', '0011', '0100', '0111', '0010', '1100', '0001', '1010', '1110', '1001'], ['1010', '0110', '1001', '0000', '1100', '1011', '0111', '1101', '1111', '0001', '0011', '1110', '0101', '0010', '1000', '0100'], ['0011', '1111', '0000', '0110', '1010', '0001', '1101', '1000', '1001', '0100', '0101', '1011', '1100', '0111', '0010', '1110']], [['0010', '1100', '0100', '0001', '0111', '1010', '1011', '0110', '1000', '0101', '0011', '1111', '1101', '0000', '1110', '1001'], ['1110', '1011', '0010', '1100', '0100', '0111', '1101', '0001', '0101', '0000', '1111', '1010', '0011', '1001', '1000', '0110'], ['0100', '0010', '0001', '1011', '1010', '1101', '0111', '1000', '1111', '1001', '1100', '0101', '0110', '0011', '0000', '1110'], ['1011', '1000', '1100', '0111', '0001', '1110', '0010', '1101', '0110', '1111', '0000', '1001', '1010', '0100', '0101', '0011']], [['1100', '0001', '1010', '1111', '1001', '0010', '0110', '1000', '0000', '1101', '0011', '0100', '1110', '0111', '0101', '1011'], ['1010', '1111', '0100', '0010', '0111', '1100', '1001', '0101', '0110', '0001', '1101', '1110', '0000', '1011', '0011', '1000'], ['1001', '1110', '1111', '0101', '0010', '1000', '1100', '0011', '0111', '0000', '0100', '1010', '0001', '1101', '1011', '0110'], ['0100', '0011', '0010', '1100', '1001', '0101', '1111', '1010', '1011', '1110', '0001', '0111', '0110', '0000', '1000', '1101']], [['0100', '1011', '0010', '1110', '1111', '0000', '1000', '1101', '0011', '1100', '1001', '0111', '0101', '1010', '0110', '0001'], ['1101', '0000', '1011', '0111', '0100', '1001', '0001', '1010', '1110', '0011', '0101', '1100', '0010', '1111', '1000', '0110'], ['0001', '0100', '1011', '1101', '1100', '0011', '0111', '1110', '1010', '1111', '0110', '1000', '0000', '0101', '1001', '0010'], ['0110', '1011', '1101', '1000', '0001', '0100', '1010', '0111', '1001', '0101', '0000', '1111', '1110', '0010', '0011', '1100']], [['1101', '0010', '1000', '0100', '0110', '1111', '1011', '0001', '1010', '1001', '0011', '1110', '0101', '0000', '1100', '0111'], ['0001', '1111', '1101', '1000', '1010', '0011', '0111', '0100', '1100', '0101', '0110', '1011', '0000', '1110', '1001', '0010'], ['0111', '1011', '0100', '0001', '1001', '1100', '1110', '0010', '0000', '0110', '1010', '1101', '1111', '0011', '0101', '1000'], ['0010', '0001', '1110', '0111', '0100', '1010', '1000', '1101', '1111', '1100', '1001', '0000', '0011', '0101', '0110', '1011']]]
for i in stable:
    for j in i:
        print(j)
    print("")





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

"""
