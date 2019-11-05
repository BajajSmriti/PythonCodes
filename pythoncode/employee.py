class Employee:
    """ This is employee class """
    empCount = 0


    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount+= 1


  
    def displayEmployee(self):
        print("Name : ",self.name)
        print("Salary : ",self.salary)

emp1 = Employee("vijay",2000)
emp2 = Employee("vikas",3000)

emp1.displayEmployee()
emp2.displayEmployee()

print("total employees ", Employee.empCount)

emp1.age= 7

print("Class documentation string :",Employee.__doc__)
print("class name:",Employee.__name__)
print("module name:",Employee.__module__)
print("list of base class:",Employee.__bases__)
print("dictonary:",Employee.__dict__)

 
