def flattenlist(a,result = None):
    #nested list become flatten list
    if result is None:
        result = []
    for x in a:
        if type(x) == list:
            flattenlist(x,result)
        else:
            result.append(x)
    return result     


def r_max(nxs):
    largest = None
    first_time = True
    for e in nxs:
        if type(e) == list:
            val = r_max(e)
        else:
            val = e
    if first_time or val > largest:
        largest = val
        first_time = False
    return largest      

def r_sum(nested_num_list):
    tot = 0
    for element in nested_num_list:
        if type(element)  == list:
            tot += r_sum(element)
        else:
            tot += element
    return tot                         