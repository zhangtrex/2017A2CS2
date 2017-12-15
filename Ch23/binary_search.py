def BinarySearch(List, number):
    Found = False
    Last = len(List) - 1
    First = 0
    Index = 0
    while Found == False:
        if number == List[(First+Last)//2]:
            Found  = True
        elif number > List[(First+Last)//2]:
            First = (First + Last)//2
        elif number < List[(First+Last)//2]:
            Last = (First + Last)//2
    if Found == True:
        return ('Found at index', (First+Last)//2+1)
    else:
        return ('Not Found')

# copy and run BinarySearch(List = [12,19,23,27,33,37,41,45,56,59,60,62,71,75,80,84,88,92,99], number = 37)
