def non_alphanumeric_counter(string):
    if string == "":
        return 0
    else:
        if string[0].isalpha() or string[0].isnumeric():
            return  non_alphanumeric_counter(string[1:] )
        else:
            counter = 0
            counter = counter + 1
            return counter + non_alphanumeric_counter(string[1:])  
                  

print(non_alphanumeric_counter("&1ac*b1 d-4!+"))
