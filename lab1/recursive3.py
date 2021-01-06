def sum_of_nested_list(mylist):
    if len(mylist) == 0:
        return 0
    else:
        if isinstance(mylist[0],list):
            return sum_of_nested_list(mylist[0]) + sum_of_nested_list(mylist[1:])
        else:    
            return mylist[0] + sum_of_nested_list(mylist[1:])


print(sum_of_nested_list([1,2,3,[4,5]]))
