class Animal():
    def __init__(self):
        pass

    def message(self):
        print("i am a animal")

class Lion(Animal):
    def __init__(self):
        super(Lion,self).__init__()

    def message(self):
        print("i am a lion")
        super(Lion,self).message()

lionl1= Lion()
lionl1.message()
