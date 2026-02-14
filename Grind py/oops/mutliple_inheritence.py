class Father:
    def money(self):
        print("Father has money")

class Mother:
    def care(self):
        print("Mother gives care")

class Child(Father, Mother):
    def enjoy(self):
        print("Child enjoys")

obj = Child()
obj.money()  # from Father
obj.care()  # from Mother
obj.enjoy() # from Child
