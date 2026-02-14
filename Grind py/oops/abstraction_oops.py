class Car:
    def __init__(self):
        self.clutch=False
        self.acc=False
        self.brake=False
    def start(self):
        self.clutch=True
        self.acc=True               #here only the neccessary things are displayed to user  
        print("Car Started..")      #unneccessaty infos are hidden to user
                                    #only printed that car started (clutch, acc, brake status are hidden)
c1=Car()
c1.start()                          