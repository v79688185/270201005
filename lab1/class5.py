class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def get_name(self): 
        return self.name

    def get_salary(self):
        return self.salary  

    def set_name(self,name):
        self.name = name

    def set_salary(self,salary):
        self.salary = salary

    def display_info(self):
        print("Name:",self.name)
        print("Salary",self.salary)    
       


class Company:
    def __init__(self,named_employee_list):
        self.named_employee_list = named_employee_list

    def get_named_employee_list(self):
        return self.named_employee_list

    def set_named_employee_list(self,named_employee_list):
        self.named_employee_list = named_employee_list

    def add_employee(self,new_employee):
        if isinstance(new_employee,Employee):
            self.named_employee_list.append(new_employee)

    def calculate_average_salary(self):
        total_salary = 0
        for employee in self.named_employee_list:
            total_salary += employee.salary
        avg_salary = total_salary / len(self.named_employee_list)
        return avg_salary    

    def display_all_info(self):
        for employee in self.named_employee_list:
            employee.display_info()  

company = Company([])
E1 = Employee("A",100)
E2 = Employee("B",3000)
E3 = Employee("C",23412)

company.add_employee(E1)
company.add_employee(E2)
company.add_employee(E3)
print(company.calculate_average_salary())

employees = [E1,E2,E3]
company.set_named_employee_list(employees)
employees = employees[:2]
print(employees is company.named_employee_list)

company.display_all_info()