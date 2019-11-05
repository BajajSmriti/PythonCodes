class time:

    def __init__(self):
        self.hh=0
        self.mm=0
        self.ss=0

    def accept(self,hh,mm,ss):
        self.hh=hh
        self.mm=mm
        self.ss=ss

    def convert(self):
        self.ss=self.hh*60*60 + self.mm*60 +self.ss

    def display(self):
        self.convert()
        print("seconds:",self.ss)
