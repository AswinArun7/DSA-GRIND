class Hospital:
    def __init__(self,hospital_name,location,started_year):
        self.hospital_name=hospital_name
        self.location=location
        self.started_year=started_year

    def show_details(self):
        print("Hospital Name:",self.hospital_name,", Location:",self.location,", Started Year:",self.started_year)

    def no_of_years(self):
        current_year=2026
        years=current_year - self.started_year
        print(self.hospital_name,"has been operating for",years,"years.")

class Humans:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_details(self):
        print("Name:",self.name,", Age:",self.age)
    def is_adult(self):
        if self.age >= 18:
            print(self.name,"is an adult.")
        else:
            print(self.name,"is not an adult.")
                    
class Doctor(Humans):
    def __init__(self,name,age,specialization,experinece,hospital):
        super().__init__(name,age)
        self.specialization=specialization
        self.experinece=experinece
        self.hospital=hospital   

    def show_details(self):
        print("Doctor Name:",self.name,", Specialization:",self.specialization,", Experience:",self.experinece,"years")    
    def Expertise(self):
        if self.experinece > 10:
            print(self.name,"is a senior expert in",self.specialization)
        else:
            print(self.name,"is a junior expert in",self.specialization)

class Patient(Humans):
    def __init__(self,name,age,illness,hospital):
        super().__init__(name,age)
        self.ailment=illness
        self.hospital=hospital 

    def show_details(self):
        print("Patient Name:",self.name,", Age:",self.age,", Illness:",self.ailment)               

    def insurance(self):
        if self.age < 18:
            print(self.name,"is eligible for child health insurance.")
        elif 18 <= self.age <= 60:
            print(self.name,"is eligible for adult health insurance.")
        else:
            print(self.name,"is eligible for senior citizen health insurance.")


h1=Hospital("City Care","New York",2000)
h1.no_of_years()

d1=Doctor("Dr. Smith",45,"Cardiology",15,h1)
d1.Expertise()

p1=Patient("Alice",30,"Flu",h1)
p1.insurance()

for person in(d1, p1):
    person.show_details()