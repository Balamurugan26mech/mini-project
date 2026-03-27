class stu:
    def __init__(self,name,regno,phone,address,branch):
        self.name=name
        self.regno=regno
        self.phone=phone
        self.address=address
        self.branch=branch

    def display(self):
        print("name",self.name)
        print("regno",self.regno)
        print("phone",self.phone)
        print("address",self.address)
        print("branch",self.branch)

a=stu("bala","192314001","9940288557","chennai","mech")
b=stu("sanjay","192314017","8270233323","chennai","mech")
c=stu("mandi","192314019","9894789838","vellore","mech")

a.display()
b.display()
c.display()