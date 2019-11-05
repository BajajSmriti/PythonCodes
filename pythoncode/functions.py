def printinfo(name,age):
    print("Name ",name)
    print("Age ",age)
    return;

printinfo(age = 50,name ="Jack")

print("----------------------------------------------")

#default args

def printinfodefault(name,age=55):
    print("Name ",name)
    print("Age ",age)
    return;

printinfodefault("Jack")

print("----------------------------------------------")


#variable length args

def printinfovariable(arg1,*vartuple):
    print("output is :")
    print(arg1)
    for var in vartuple:
        print(var)
    return

printinfovariable(10)
printinfovariable(10,20,30,40)

print("----------------------------------------------")


#anonymous function or lambda function

#lambda [arg1,arg2,arg3,....,argn]: expression

total = lambda arg1,arg2 : arg1 + arg2

print(total(2,3))

print("----------------------------------------------")


#some more lambda

foo = [2,3,4,5,6,22,17,12,34]

print(list(map(lambda x : x*2,foo)))

print(list(filter(lambda x : x%3==0,foo)))

print(list(filter(lambda x : x%3==0,range(2,100))))

print("----------------------------------------------")


#named variable

def print_prm(**params):
    print(params)

print_prm(x=1,y=2,z=1)

print("----------------------------------------------")




# mixed of all

def print_mix_all(x,y,*pospar,**keypar):
    print(x,y)
    print(pospar)
    print(keypar)

print_mix_all(1,2,3,4,5,a=1,b=2)

print("----------------------------------------------")


#modify global variable

money = 2000
def addmoney():
    global money
    money=money+1
    a=5
    print(locals())
    print(globals())

addmoney()
print("----------------------------------------------")

    

    
          
