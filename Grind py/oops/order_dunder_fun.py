#Create a class Order with attributes item and price.
#Use dunder function __gt__()to convey that:
# order1 > order2 if order1.price > order2.price 

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,odr2):
        return self.price > odr2.price

odr1=Order("snacks",20)
odr2=Order("tea",15)

print(odr1>odr2)  #calls __gt__ method -> compares prices of odr1 and odr2