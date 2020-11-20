list=[]
sum = 0
number_Of_Value = int(input("Enter the number of values: "))
for i in range(number_Of_Value):
  value=int(input("Enter the value: "))
  sum += value
  list.append(sum)
  list.sort()
  list.reverse()
  print(list)