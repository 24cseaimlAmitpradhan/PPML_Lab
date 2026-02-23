class number:
    def __init__(self,value):
        self.value=value
    def __sub__(self,other):
        return number(self.value-other.value)
    def display(self):
        print("sub:",self.value)
n1=number(10)
n2=number(20)
n3=n1-n2
n3.display()