def sum_of_lists(mylist):
    if len(mylist) == 0:
        return 0
    else:
        return mylist[0] + sum_of_lists(mylist[1:])  

print(sum_of_lists([12, -7, 5, -89.4, 3, 27, 56, 57.3]))          