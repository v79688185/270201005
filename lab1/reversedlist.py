def reverselist(mylist):
    if len(mylist) == 0:
        return []
    else:
        return [mylist[-1]] + reverselist(mylist[0:-1])   
print(reverselist([1,2,3,4]))        