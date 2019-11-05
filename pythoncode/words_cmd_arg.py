"""
this modules handles command line arguments
"""
import sys

def printwords(items):
    """this function iterates using for
     args : it takes one arg
     return : nothing
     """
    
    for eachitem in items:
        print(eachitem)

def main(argument):
    printwords(argument)
    print(sys.argv[0])

if __name__ == '__main__':
    main(sys.argv[1])
    
    
