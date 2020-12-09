element_List = []
n = int(input("Enter number of element: "))
while n-1 >= 0:
  element =eval(input("Enter the element:"))
  n-=1
  element_List.append(element)
print(element_List)
for value in element_List:
  if element_List.count(value)>1:
    element_List.remove(value)
print(element_List)    