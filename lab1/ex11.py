a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
d = (b**2)-(4*a*c)
if d<0:
  print("There are two complex roots.")
elif d==0:
  print("There is one real root.")
elif d>0:
  print("There are two real roots.")  
