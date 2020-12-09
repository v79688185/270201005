numbers1 = [2,3,4,20,5,5,15]
numbers2 = [10,20,20,15,30,40]
numbers1_sets = set(numbers1)
numbers2_sets = set(numbers2)
union_list = list()
print(numbers1_sets)
print(numbers2_sets)
for element in numbers1_sets:
  for element2 in numbers2_sets:
    if element == element2:
      print(element)
    else:
      pass  
for element in numbers1: 
  union_list.append(element)   
for element2 in numbers2:
  union_list.append(element2)
union_set = set(union_list)  
print(union_set)