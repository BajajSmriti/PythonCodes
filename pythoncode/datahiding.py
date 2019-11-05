class Justcounter:
    __secretcount = 0


    def count(self):
        self.__secretcount +=1
        print(self.__secretcount)
       

counter = Justcounter()
counter.count()
counter.count()
print(counter._Justcounter__secretcount)
    
