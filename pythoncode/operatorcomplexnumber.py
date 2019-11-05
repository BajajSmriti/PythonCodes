class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __mul__(self, other):
        return complex(self.real*other.real-self.imag*other.imag, self.real*other.imag+self.imag*other.real)
   

print ("Enter real and imaginary part of complex No - 1(separeated by space)") 
A = complex(*map(float, raw_input().strip().split()))
print ("Enter real and imaginary part of complex No - 2(separeated by space)") 
B = complex(*map(float, raw_input().strip().split()))

print ("Multiplication: " + str(A*B))

