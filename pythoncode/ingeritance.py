class Parent():
    parentattr = 100
    def __init__(self):
        print("calling parent init")


    def parentMethod(self):
        print("calling parent method")


    def setAttr(self,attr):
        Parent.parentAttr = attr


    def getAttr(self):
        print("parent attr : ", Parent.parentAttr)


class Child(Parent):
   
    def __init__(self):
        print("calling child init")


    def childMethod(self):
        print("calling child method")

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()

        
