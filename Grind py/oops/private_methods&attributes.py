class Account:
    def __init__(self,acc_no, password):
        self.account_no=acc_no
        self.__password=password    #private attribute __ before attribute name makes it private

s1=Account(12345, "mypassword")
print(s1.account_no)    
# print(s1.password)    #accesing private attribute outside the class will give error


class Person:
    __name = "John"        #private attribute

    def __hello(self):
        print("Hello person!")

    def welcome(self):
        self.__hello()      #accessing private method inside the class

p1=Person()
# p1.hello()          #accessing private method outside the class will give error

p1.welcome()    