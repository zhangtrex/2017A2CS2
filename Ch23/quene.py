#Kevin Yang from Option 1
# NP for NullPointer, FLP for FreeListPointer
#SP for StartPointer
#RP for Rear pointer
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
    global RP
    global L 
    
    NP = -1
    L = [0,0,0,0,0,0,0,0,0,0]
    FLP = 0
    SP = NP
    RP = 0
    for i in range (9):
        L[i] = List(None, i+1)
    L[9] = List(None, NP)
    
def Queue(V):
    global FLP
    global SP
    global RP
    if SP == NP:
        L[0] = List(V, NP)
        FLP = 1
        SP = 0
        RP = 0
    else:
        F = L[FLP].pointer
        L[FLP] = List(V, NP)
        L[RP].pointer = FLP
        RP = FLP
        FLP = F

        
        
def De_Queue():
    global FLP
    global SP
    global RP
    if SP == NP:
        return 0
    else:
        FLP = SP
        F = L[SP].pointer
        L[SP].pointer = L[FLP].pointer
        SP = F

def PrintQueue():
    P = SP
    while P != -1:
        print(L[P].value)
        P = L[P].pointer
        
InitialiseList()
Queue(4)

Queue(7)

Queue(20)

Queue(79)

Queue(23)

Queue(63)

PrintQueue()
print('after DE-QUEUE')

De_Queue()

PrintQueue()
