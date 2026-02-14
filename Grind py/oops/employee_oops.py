#Define an Employee class with attributes role, dept and salary.This class also has a show_details() method.
#create an Engineer class that inherits from Employee & and has additional attributes name and age.

class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def show_details(self):
        print("Role:",self.role)
        print("Department:",self.dept)
        print("Salary:",self.salary)

class Engineer(Employee):
    def __init__(self,name ,age):

        self.name=name
        self.age=age
        super().__init__("Engineer","IT",40000)

eng1=Engineer("Aswin",21)
print(eng1.show_details())