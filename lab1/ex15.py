a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
same_units = 0
while a>0 and b>0:
    if a % 10 == b % 10:
      same_units+=1
    a = a // 10
    b = b // 10
print(same_units)    
