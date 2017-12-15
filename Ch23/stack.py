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

def PrintStack():
    P = SP
    while P != -1:
        print(L[P].value)
        P = L[P].pointer

def Push(V):
    global FLP
    global SP
    if FLP != NP:
        NNP = FLP
        FLP = L[FLP].pointer
        L[NNP].pointer = SP
        SP = NNP
        L[NNP].value = V

def Pop():
    global FLP
    global SP
    if SP != NP:
        TNP = SP
        FLP = TNP
        SP = L[TNP].pointer
        