#define a circle class to create a circle with radius r using the constructor.
#Define an Area() method of the class which calculates the area if the circle.
#Define a Perimeter() method of the class which allows to to calculate the perimeter of the circle.


class Circle:
    def __init__(self,r):
        self.r=r

    def Area(self):
        return 3.14*self.r*self.r

    def Perimeter(self):
        return 2*3.14*self.r

c1=Circle(5)
print(c1.r)
print(c1.Area())
print(c1.Perimeter())


 