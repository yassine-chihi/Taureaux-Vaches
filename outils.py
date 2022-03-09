# ©CopyRight : Walid Oualili & Yassine Chihi
import random

def IntToList(n):
    return [int(i) for i in str(n)]

def est_differents(num):
    lst = IntToList(num)
    if len(lst) == len(set(lst)):     # SET : return unique and different elements
        return True
    else:
        return False

def CodeSecret(): 
    while True: 
        num = random.randint(1000,9999) 
        if est_differents(num): 
            return num

def TaureauxVaches(num,guess):
    T_V = [0,0]
    numLst = IntToList(num)
    guessLst = IntToList(guess)
    for i,j in zip(numLst,guessLst):
        if j in numLst:
            if j==i:
                T_V[0]+=1
            else:
                T_V[1]+=1
    return T_V
