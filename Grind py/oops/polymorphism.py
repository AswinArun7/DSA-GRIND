class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def show_num(self):
        print(self.real,"+",self.imag,"j")

    def __add__(self,num2):                 #operator overloading (__add__ instead of add)
        newreal=self.real+num2.real
        newimag=self.imag+num2.imag
        return Complex(newreal,newimag)

num1=Complex(5,6)
num1.show_num()
num2=Complex(3,4)
num2.show_num()
                            
num3=num1+num2              #calls __add__ method   //avoids ->num3=num1.add(num2))
num3.show_num()