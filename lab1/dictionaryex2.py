employess_dict = dict()
salary_list = list()
for i in range(5):
  name = input("Enter the name: ")
  salary = int(input("Enter salaries: "))
  salary_list.append(salary)
  employess_dict[name] = salary
print(employess_dict)
salary_list.sort()
salary_list.reverse()
for value in salary_list[0:3]:
  salary = value
  print(name,value)
