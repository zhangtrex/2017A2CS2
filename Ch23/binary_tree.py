# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 11:46:02 2017

@author: Kevin Young from Option 1
"""
# Lpointer represents smaller value
# Rpointer represents larger value

class List(object):
    def __init__(self, value, Lpointer, Rpointer):
        self.value = value
        self.Lpointer = Lpointer
        self.Rpointer = Rpointer
    def __str__(self):
        return "(%s,%s,%s)"%(self.value, self.Lpointer,self.Rpointer)

def InitialiseBinaryTree():
    global FLP
    global SP
    global T 
    global LNP
    global RNP
    global NP
    global RP
    NP = -1
    FLP = 0
    RP = NP
    T = [0,0,0,0,0,0,0,0,0,0]
    for i in range (9): 
        T[i] = List(None, i+1,-1)
    T[9] = List(None, NP, NP)

    
def InsertBinaryTree(V):
    global FLP
    global SP
    global RP
    TurnLeft = False
    TurnRight = False
    if FLP != NP:
        NNP = FLP
        FLP = T[FLP].Lpointer
        T[NNP].value = V
        T[NNP].Lpointer = NP
        T[NNP].Rpointer = NP
        if RP == NP:
            RP = NNP
        else:
            TNP = RP
            while TNP != NP:
                PNP = TNP
                if T[TNP].value > V:
                    TurnLeft = True
                    TNP = T[TNP].Lpointer
                else:
                    TurnRight = True
                    TNP = T[TNP].Rpointer
            if TurnLeft == True:
                T[PNP].Lpointer = NNP
            elif TurnRight == True:
                T[PNP].Rpointer = NNP
                
                
def FindNode(V):
    global FLP
    global SP
    global RP
    TNP = RP
    while TNP != NP and T[TNP].value != V:
        if T[TNP].value > V:
            TNP = T[TNP].Lpointer
        else:
            TNP = T[TNP].Rpointer
    return TNP