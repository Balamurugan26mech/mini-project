class stu :
    def __init__(self,mark):
        self.mark=mark

    def update(self,new_mark):
        self.mark=new_mark
    def show(self):
        print("mark",self.mark)

s1=stu(80)
s1.update(95) 
s1.show()