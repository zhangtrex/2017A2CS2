#Kevin Yang from Option 1
# NP for NullPointer, FLP for FreeListPointer
#SP for StartPointer
#L for a list, V for Value
# NNP for NewNodePointer
#CV for CompareValue
#TNP for ThisNodePointer

class List(object):
    def __init__(self, value, pointer):
        self.value = value
        self.pointer = pointer
    def __str__(self):
        return "(%s,%s)"%(self.value, self.pointer)

def InitialiseList():
    global FLP
    global NP
    global SP
    global L 
    NP = -1
    L = [0,0,0,0,0,0,0,0,0,0]
    FLP = 0
    SP = NP
    for i in range (9):
        L[i] = List(None, i+1)
    L[9] = List(None, NP)

def PrintList():
    P = 0
    while P != -1:
        print(L[P].value)
        P = L[P].pointer

def InsertList(V):
    global FLP
    global SP
    if FLP != NP:
        NNP = FLP
        L[NNP].value = V
        CV = NP
        FLP = L[FLP].pointer
        TNP = SP
        while TNP != NP and L[TNP].value < V:
            CV = TNP
            TNP = L[TNP].pointer
        if CV == NP:
            L[NNP].pointer =  SP
            SP = NNP
        else:
            L[NNP].pointer = L[CV].pointer
            L[CV].pointer = NNP

def FindValue(V):
    global SP
    TNP = SP
    while TNP != NP and L[TNP].value <= V:
         if L[TNP].value == V:
             return TNP
         else:
             TNP = L[TNP].pointer
    return NP

def DeleteList(V):
    global FLP
    global SP
    TNP=SP
    while TNP!=NP and L[TNP].value !=V:
        CV = TNP
        TNP = L[TNP].pointer
    if TNP!=NP:
        if TNP==SP:
            SP=L[SP].pointer
        else:
            L[CV].pointer=L[TNP].pointer
        L[TNP].pointer=FLP
        FLP = TNP
