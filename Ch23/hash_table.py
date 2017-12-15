# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 14:22:20 2017

@author: Kevin Young from Option One 
"""
C = 0
def InitialiseHash():
    global H
    H = [None for i in range (10)]

def InsertHash(V):
    global H
    global M
    global C
    M = V % 10
    A = False
    B = 0
    while A != True and B <= 10 :
        if M == 10 and C == 1 :
            M = 0
        else:
            M = M + 1
            if H[M-1] == None:
                H[M-1] = V
                if V % 10 == 9:
                    C = 1
                A = True
            else:
                A = False
        B = B + 1
    if B > 10:
        print ('the Hash is full')
                    
def PrintHash():
    global H
    for i in range (10):
        print(H[i])

def SearchHash(V):
    global H
    M = V % 10
    A = False
    B = 0
    while A != True and B <= 10 :
        if M == 9:
            M = 0
        else: 
            M = M + 1
            if H[M-1] == V:
                A = True
            else:
                A = False
        B += 1
    if B > 10 and A == False:
        print ('Not Found')
    elif B <= 10 and A == True: 
        return 'the value has found, the index of the value is', M-1