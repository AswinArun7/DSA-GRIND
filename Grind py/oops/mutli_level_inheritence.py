class A:
    def feature1(self):
        print("Feature 1 from A")

class B(A):
    def feature2(self):
        print("Feature 2 from B")

class C(B):
    def feature3(self):
        print("Feature 3 from C")

obj = C()
obj.feature1()   # from A
obj.feature2()   # from B
obj.feature3()   # from C

n=B()
n.feature1()   # from A
n.feature2()   # from B
# n.feature3()   # This will give an error since feature3 is not in B