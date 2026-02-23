class father():
    def skill1(self):
        print("father class")
class mother():
    def skill2(self):
        print("mother class")
class child(father,mother):
    def skill3(self):
        print("child class")
c=child()
c.skill1()
c.skill2()
c.skill3()