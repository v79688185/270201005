list=[]
high_Value = int(input("Enter the high value: "))
low_Value = int(input("Enter the low value: "))
n = high_Value - low_Value - 1
for i in range(0,100):
  if i % n == 0:
    list.append(i)
print(list)