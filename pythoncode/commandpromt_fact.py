import sys

def fact(x):
    
    ans=1
    x=input("Enter no")
    while(x!=0):
        ans=ans*int(x)
        x=int(x)-1
    print(ans)


def main(x):
    fact(x)

if __name__ == '__main__':
    main(sys.argv[1])


    
