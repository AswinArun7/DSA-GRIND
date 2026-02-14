#Design an object-oriented system  for a car company by creating classes to represent a Car Company, Car Salesman, and Customer. 
#Each class should contain at least three relevant attributes and suitable member functions to perform operations related to their roles.
#iMPLEMENT INHERITANCE AND POLYMORPHISM WITHIN THIS.

class Company:
    def __init__(self,company_name,location):
        self.company_name=company_name
        self.location=location
    def role(self):     #this method will be overridden in the child classes (POLYMORPHISM)
        print("this is a car company")

    def company_details(self):
        print("Company Name:",self.company_name,", Location:",self.location)
        

class Car_salesman(Company):
    def __init__(self,salesman_name,employee_id,salary,company_name,location):
        self.salesman_name=salesman_name    
        self.employee_id=employee_id
        self.salary=salary
        super().__init__(company_name,location)

    def sell_car(self,car_model):
        print(self.salesman_name,"sold",car_model)

    def role(self):     #overriding the role method of the Company class (POLYMORPHISM)
        print("this is a car salesman")

    def salesman_details(self):
        print("Salesman Name:",self.salesman_name,", Employee ID:",self.employee_id,", Salary:",self.salary)


class Customer(Company):
    def __init__(self,customer_name,budget,company_name,location):
        self.customer_name=customer_name
        self.budget=budget
        super().__init__(company_name,location)

    def buy_car(self,car_model,price):
        if price <= self.budget:
            print(self.customer_name,"bought",car_model)
        else:
            print(self.customer_name,"does not have enough budget to buy",car_model)
            
    def role(self):   #overriding the role method of the Company class (POLYMORPHISM)
        print("this is a customer")

    def customer_details(self):
        print("Customer Name:",self.customer_name,", Budget:",self.budget)    



c1=Company("Toyota","Japan")
c1.company_details()        

s1=Car_salesman("John",101,50000,"Toyota","Japan")
s1.salesman_details()
s1.sell_car("BMW X5")

cust1=Customer("Alice",6000,"Toyota","Japan")
cust1.customer_details()
cust1.buy_car("BMW X5",55000)


for i in (c1,s1,cust1):
    i.role()