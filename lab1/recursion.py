def rec_multip(n):
    if n == 1:
        return 3
    return 3 + rec_multip(n-1)    

print(rec_multip(6))    
    