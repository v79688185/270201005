def binarysearch(n,liste):
    if len(liste) == 0:
        return -1
    else:
        mid = len(liste) // 2
        if n == liste[mid]:
            return mid 
        elif n > liste[mid]:
            return binarysearch(n,liste[mid+1:])
        elif n < liste[mid]:
            return binarysearch(n,liste[:mid])

print(binarysearch(2,[1,2,3,4,5,6,7,8]))
