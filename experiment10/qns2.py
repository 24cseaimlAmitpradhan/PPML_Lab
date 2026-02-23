class grandparent:
    def property(self):
        print("grandparents property")
class father(grandparent):
    def business(self):
        print("fathers business")
class child(father):
    def education(self):
        print("child education")
c=child()
c.business()
c.property()
c.education()