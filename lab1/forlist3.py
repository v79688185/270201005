low_Value = int(input("Enter the low value: "))
high_Value = int(input("Enter the high value: "))
for i in range(low_Value,high_Value):
  can_Divisible = False 
  for j in range(2,i):
    if i % j == 0:
      can_Divisible = True
  if can_Divisible == False:
    print(i)    