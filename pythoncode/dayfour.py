Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/employee.py 
Name :  vijay
Salary :  2000
Name :  vikas
Salary :  3000
total employees %d Employee.empCount
>>> 
 RESTART: C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/employee.py 
Name :  vijay
Salary :  2000
Name :  vikas
Salary :  3000
total employees  2
>>> 
 RESTART: C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/employee.py 
Name :  vijay
Salary :  2000
Name :  vikas
Salary :  3000
total employees  2
>>> hasattr(emp1,'age')l
SyntaxError: invalid syntax
>>>  hasattr(emp1,'age')
 
SyntaxError: unexpected indent
>>>  hasattr(emp1,'age')
KeyboardInterrupt
>>> hasattr(emp1,'age')
True
>>> getattr(emp1,'age')
7
>>> setattr(emp1,'age',10)
>>> getattr(emp1,'age')
10
>>> delattr(emp1,'age')
>>> hasattr(emp1,'age')
False
>>> 
 RESTART: C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/employee.py 
Name :  vijay
Salary :  2000
Name :  vikas
Salary :  3000
total employees  2
Class documentation string :  This is employee class 
class name: Employee
module name: __main__
list of base class: (<class 'object'>,)
dictonary: {'__module__': '__main__', '__doc__': ' This is employee class ', 'empCount': 2, '__init__': <function Employee.__init__ at 0x0000027A6B028AE8>, 'displayEmployee': <function Employee.displayEmployee at 0x0000027A6B028B70>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>}
>>> 
 RESTART: C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/ingeritance.py 
Traceback (most recent call last):
  File "C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/ingeritance.py", line 28, in <module>
    c = child()
NameError: name 'child' is not defined
>>> 
 RESTART: C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/ingeritance.py 
calling child init
calling child method
calling parent method
Traceback (most recent call last):
  File "C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/ingeritance.py", line 32, in <module>
    c.getAttr()
TypeError: getAttr() missing 1 required positional argument: 'attr'
>>> 
 RESTART: C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/ingeritance.py 
calling child init
calling child method
calling parent method
parent attr :  200
>>> issubclass(Child,Parent)
True
>>> isinstance(c,Child)
True
>>> 
 RESTART: C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/overriding.py 
i am a lion
i am a animal
>>> 
 RESTART: C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/overriding.py 
i am a lion
>>> 
 RESTART: C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/employee.py 
Name :  vijay
Salary :  2000
Name :  vikas
Salary :  3000
total employees  2
Class documentation string :  This is employee class 
class name: Employee
module name: __main__
list of base class: (<class 'object'>,)
dictonary: {'__module__': '__main__', '__doc__': ' This is employee class ', 'empCount': 2, '__init__': <function Employee.__init__ at 0x0000023032D58AE8>, 'displayEmployee': <function Employee.displayEmployee at 0x0000023032D58B70>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>}
>>> 
 RESTART: C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/operator_overloading.py 
Traceback (most recent call last):
  File "C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/operator_overloading.py", line 11, in <module>
    print(v1 + v2)
  File "C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/operator_overloading.py", line 7, in __add__
    return Vector(self.a + other.a+ self.b + other.b)
TypeError: __init__() missing 1 required positional argument: 'b'
>>> 
 RESTART: C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/operator_overloading.py 
Traceback (most recent call last):
  File "C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/operator_overloading.py", line 11, in <module>
    print(v1 + v2)
  File "C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/operator_overloading.py", line 7, in __add__
    return Vector(self.a + other.a+ self.b + other.b)
TypeError: __init__() missing 1 required positional argument: 'b'
>>> 
 RESTART: C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/operator_overloading.py 
Traceback (most recent call last):
  File "C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/operator_overloading.py", line 11, in <module>
    print(v1 + v2)
  File "C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/operator_overloading.py", line 7, in __add__
    return Vector(self.a + other.a+ self.b + other.b)
TypeError: __init__() missing 1 required positional argument: 'b'
>>> 
 RESTART: C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/operator_overloading.py 
Traceback (most recent call last):
  File "C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/operator_overloading.py", line 11, in <module>
    print(v1 + v2)
  File "C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/operator_overloading.py", line 7, in __add__
    return Vector(self.a + other.a+ self.b + other.b)
TypeError: __init__() missing 1 required positional argument: 'b'
>>> 
 RESTART: C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/operator_overloading.py 
Traceback (most recent call last):
  File "C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/operator_overloading.py", line 15, in <module>
    print(v1 + v2)
  File "C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/operator_overloading.py", line 11, in __add__
    return Vector(self.a + other.a+ self.b + other.b)
TypeError: __init__() missing 1 required positional argument: 'b'
>>> 
 RESTART: C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/operator_overloading.py 
Traceback (most recent call last):
  File "C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/operator_overloading.py", line 15, in <module>
    print(v1 + v2)
  File "C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/operator_overloading.py", line 11, in __add__
    return Vector(self.a + other.a+ self.b + other.b)
TypeError: __init__() missing 1 required positional argument: 'b'
>>> 
 RESTART: C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/operator_overloading.py 
Traceback (most recent call last):
  File "C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/operator_overloading.py", line 15, in <module>
    print(v1 + v2)
  File "C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/operator_overloading.py", line 11, in __add__
    return Vector(self.a + other.a+ self.b + other.b)
TypeError: __init__() missing 1 required positional argument: 'b'
>>> 
 RESTART: C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/datahiding.py 
1
Traceback (most recent call last):
  File "C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/datahiding.py", line 11, in <module>
    print(counter,__secretcount)
NameError: name '__secretcount' is not defined
>>> 
 RESTART: C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/datahiding.py 
1
Traceback (most recent call last):
  File "C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/datahiding.py", line 11, in <module>
    print(counter.__secretcount)
AttributeError: 'Justcounter' object has no attribute '__secretcount'
>>> 
 RESTART: C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/datahiding.py 
1
1
>>> 
 RESTART: C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/datahiding.py 
1
1
1
>>> 
 RESTART: C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/datahiding.py 
1
1
>>> 
 RESTART: C:/Users/A06438_p5.training/AppData/Local/Programs/Python/Python36/puthon day 4/datahiding.py 
1
2
2
>>> 
