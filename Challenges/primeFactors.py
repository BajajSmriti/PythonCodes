def factor( x ):
    list1=[]
    i=2
    while(i<=x):
        if(x%i == 0):
            list1.append(i)
            x=x/i
        else:
            i+=1
    return list1
    
print(factor(189))
