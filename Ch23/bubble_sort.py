# Kevin Yang 
def BubbleSort(List):
    for j in range(len(List)):
        for i in range (len(List)-1):
            if List[i] > List[i+1] :
                ACC = List [i]
                List[i] = List[1+i]
                List[i+1] = ACC
    return List
