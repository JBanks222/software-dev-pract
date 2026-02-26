"""
Jalen Banks
lab 9, Unit Testing
Feb 26. 2026
"""

class Employee:
    #property
    raise_amt = 1.05

    def __init__(self, firstname, lastname, salary):
        self.first = firstname
        self.last = lastname
        self.salary = salary
    @property
    def emailemployee(self):
        return f"{self.first}.{self.last}@email.com"
    
    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    
    # method
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)
    
    # local testing
    # create an instance of the class
employee1 = Employee("Jalen", "Banks", 110000)
print(employee1.emailemployee) # test email property
print(f"employee full name: {employee1.fullname}") # test fullname property
print(f"employee salary : {employee1.salary} per year") # test salary 
employee1.apply_raise()
print(f"employee salary after raise: {employee1.salary} per year") # test apply raise method
