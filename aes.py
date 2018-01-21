##  Import s box and multiplication tables
from db import *

##  Convert ascii character to it's hex value
def char2hex(c):
    return hex(ord(c))[2:]
##  Convert hex value to an ascii character
def hex2char(x):
    return chr(int(x, 16))

## Exclusive OR two hex numbers
def xor(s1, s2):
    k =  hex(int(s1, 16) ^ int(s2, 16))[2:]
    if(len(k) == 1):
        k = "0" + k
    return k
## Find decimal equivalent of a 1-digit hex number
def hashcode(c):
    if(c.isdigit()):
        return ord(c)-48
    return ord(c)-87

## Find a value's corrosponding value in the s box
def s(x):
    global sbox
    return sbox[hashcode(x[0])][hashcode(x[1])]

## Find the original value from an s box value
def inv_s(x):
    global sbox
    for i in range(0, len(sbox)):
        if x in sbox[i]:
            return hex(i)[2:] + hex(sbox[i].index(x))[2:]

##  Find which multiplication table to use
def mult_hash(x):
    if(x == 2):
        return 0
    if(x == 3):
        return 1
    if(x == 9):
        return 2
    if(x == 11):
        return 3
    if(x == 13):
        return 4
    if(x == 14):
        return 5

##  Multiply a number in a multiplication table
def mult(a, b):
    return mults[mult_hash(a)][hashcode(b[0])][hashcode(b[1])]

## Multiply two matrices
def matrix_mult(m1, m2):
    m_new = []
    for row in range(4):
        m_new.append([])
        for col in range(4):
            curr_sum = "00"
            for k in range(4):
                if(m1[row][k] == 1):
                    curr_sum = xor(curr_sum, m2[k][col])
                else:
                    curr_sum = xor(curr_sum, mult(m1[row][k], m2[k][col]))
            m_new[row].append(curr_sum)
    return m_new

## Byte sub - send everything through the s box
def bs(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = s(m[i][j])
    return m

## Undo the byte sub
def inv_bs(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = inv_s(m[i][j])
    return m

##  Run 'switch rows'
def sr(m):
    new_m = []
    for i in range(4):
        temp = []
        for j in range(4):
            temp.append(m[i][(i+j)%4])
        new_m.append(temp)
    return new_m

##  Undo 'switch rows'
def inv_sr(m):
    new_m = []
    for i in range(4):
        temp = []
        for j in range(4):
            temp.append(m[i][(j-i)%4])
        new_m.append(temp)
    return new_m

##  Run 'mix columns', scramble matrix by multiplying it with another 
def mc(m):
    left_m = [[2, 3, 1, 1],[1, 2, 3, 1],[1, 1, 2, 3],[3, 1, 1, 2]]
    return matrix_mult(left_m, m)

##  Undo 'mix columns' by multiplying with another matrix
def inv_mc(m):
    left_m = [[14,11,13,9],[9,14,11,13],[13,9,14,11],[11,13,9,14]]
    return matrix_mult(left_m, m)

## Add Round Key
def ark(matrix, key):
    for x in range(4):
        for y in range(4):
            matrix[x][y] = xor(matrix[x][y], key[x][y])
    return matrix

##  Helper method for generating key schedule
def T(key, j):
    table = {4 : 0b00000001, 8 : 0b00000010, 12 : 0b00000100, 16 : 0b00001000,\
             20 : 0b00010000, 24 : 0b00100000, 28 : 0b01000000, 32 : 0b10000000,\
             36 : 0b00011011, 40 : 0b00110110}
    out = []
    for i in range(4):
        out.append(key[i][j-1])
    if j in table.keys():#% 4 == len(key):
        out.append(out[0])
        out = out[1:]
        for i in range(4):
            out[i] = s(out[i])
        out[0] = hex(int(out[0], 16) ^ int(table[j]))[2:]
    return out

##  Generate the full set of keys from the original key
def expandKeySchedule(key):
    for j in range(4, 44):
        t = T(key, j)
        for i in range(4):
            key[i].append(xor(key[i][j-4], t[i]))

##  Return the key for the current step from the list of keys
def getCurrKey(k, r):
    r = 4*r
    return [k[0][r:r+4],k[1][r:r+4],k[2][r:r+4],k[3][r:r+4]]

##  Convert a key string to a matrix of hex values; needed to run encryption operations
def keyToMatrix(string):
    k = [['', '', '', ''],
         ['', '', '', ''],
         ['', '', '', ''],
         ['', '', '', '']]
    
    string = string + 'ZZZZZZZZZZZZZZZZ'
    i = 0
    for x in range(4):
        for y in range(4):
            k[y][x] = char2hex(string[i])
            i += 1
    return k

##  Convert a string to a matrix of hex values; needed to run encryption operations
def strToMatrices(s):
    mats = []
    while(len(s) % 16 != 0):
        s = s + 'Z'
    for n in range(0, len(s), 16):
        curr_mat = []
        for i in range(4):
            curr_row = []
            for j in range(4):
                curr_row.append(char2hex(s[n+4*i+j]))
            curr_mat.append(curr_row)
        mats.append(curr_mat)
    return mats

##  Convert a matrix of hex values to the corrosponding string
def matricesToStr(mats):
    s = ""
    for n in range(len(mats)):
        for i in range(4):
            for j in range(4):
                s = s + hex2char(mats[n][i][j])
    return s

##  Take a string to encode and a string as a key and encode
def encryptAES(s, k):
    mats = strToMatrices(s)
    key = keyToMatrix(k)
    expandKeySchedule(key)
    curr_round = 0
    curr_key = getCurrKey(key, curr_round)
    for i in range(len(mats)):
        mats[i] = ark(mats[i], curr_key)
    while(curr_round < 10):
        curr_round += 1
        curr_key = getCurrKey(key, curr_round)
        for i in range(len(mats)):
            mats[i] = bs(mats[i])
            mats[i] = sr(mats[i])
            if(curr_round < 10):
                mats[i] = mc(mats[i])
            mats[i] = ark(mats[i], curr_key)
    return mats

##  Take encrypted data as list of matrices and run decrypt on it
def decryptAES(mats, k):
    key = keyToMatrix(k)
    expandKeySchedule(key)
    curr_round = 10
    while(curr_round > 0):
        curr_key = getCurrKey(key, curr_round)
        for i in range(len(mats)):
            mats[i] = ark(mats[i], curr_key)
            if(curr_round != 10):
                mats[i] = inv_mc(mats[i])
            mats[i] = inv_sr(mats[i])
            mats[i] = inv_bs(mats[i])
        curr_round -= 1
    curr_key = getCurrKey(key, curr_round)
    for i in range(len(mats)):
        mats[i] = ark(mats[i], curr_key)
    return matricesToStr(mats)

st = "Sgt. Pepper's Lonely Hearts Club Band"
key = "The Beatles"

##st = "My house is full of traps"
##key = "Horse in aisle 5"

##st = "It is Wednesday, my dudes"
##key = "Please don't"

##st = "We choose to do all these things, not because they are easy, but because they are hard"
##key = "Saturn V"

print('Original message:\n' + st)
e = encryptAES(st, key)
print("Encrypted message:\n" + matricesToStr(e))
s = decryptAES(e, key)
print("Decrypted message:\n" + s)
            
