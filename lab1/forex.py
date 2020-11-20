number_of_value = int(input("Enter the number of value: "))
sum=0
for n in range(number_of_value):
  value = int(input("Enter the value: "))
  sum+=value
average=sum/number_of_value
print(average)