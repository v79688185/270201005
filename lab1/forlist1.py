list=[]
number_Of_Value = int(input("Enter the number of values: "))
for i in range(number_Of_Value):
  value=int(input("Enter the value: "))
  square = value ** 2
  list.append(square)
  list.sort()
  list.reverse()
print(list)