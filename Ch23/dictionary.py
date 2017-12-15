# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 15:34:56 2017

@author: Kevin Young
"""

class D(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value 
    def __str__(self):
        return "(%s,%s)"%(self.key, self.value)
    
C = 0

def InitialiseDict():
    global H
    H = [0 for i in range (20)]
    for i in range (20):
        H[i] = D(None, None)

def Insert(V, V2):
    global H
    global M
    global C
    L = ord(V[0])
    M = L % 20
    A = False
    B = 0
    while A != True and B <= 20 :
        if M == 20 and C == 1 :
            M = 0
        else:
            M = M + 1
            if H[M-1].key == None:
                H[M-1].key = V
                H[M-1].value = V2
                if L % 20 == 19:
                    C = 1
                A = True
            else:
                A = False
        B = B + 1
    if B > 20:
        print ('the Hash is full')

def Search(V):
    global H
    global C
    global M
    L = ord(V[0])
    M = L % 20
    A = False
    B = 0
    while A != True and B <= 20 :
        if M == 20 :
            M = 0
        else: 
            M = M + 1
            if H[M-1].key == V:
                A = True
                if L % 20 == 19:
                    C = 1
            else:
                A = False
        B += 1
    if B > 20 and A == False:
        print ('Not Found')
    elif B <= 20 and A == True: 
        return 'the value has found, the index of the value is', M-1
    
InitialiseDict()
Insert('CU', 'Control Unit')

Insert('IP', 'Internet Protocol')

Insert('RAM', 'random access memory')

for i in range (20):
    print(H[i])