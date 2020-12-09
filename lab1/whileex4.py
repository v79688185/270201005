more_value1="yes"
more_value = input("Do you want to more value yes or no: ")
count=0
sum=0
while more_value == more_value1:
  x=int(input("Enter the value: "))
  more_value = input("Do you want to more value yes or no: ")
  count+=1
  sum+=x
print("average is", sum/count)