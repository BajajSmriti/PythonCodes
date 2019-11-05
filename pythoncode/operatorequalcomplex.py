class Vector:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

        
    def __str__(self):
        return 'Vector (%d , %d)' % (self.real,self.imag)

    def __eq__(self,other):
        return Vector(self.real*other.real-self.imag*other.imag, self.real*other.imag+self.imag*other.real)

v1= Vector(3,2)
v2= Vector(1,4)
print(v1 == v2)



