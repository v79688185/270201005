def getevens(mylist):
    if len(mylist) == 0:
        return 0
    else: 
        if mylist[0] % 2 == 0:
            return 1 + getevens(mylist[1:])
        else:
            return getevens(mylist[1:])   

print(getevens([0,1,2,3,4,5]))