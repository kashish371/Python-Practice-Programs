class student():
    institution="IIPS"
    
    def __init__(self, a, b):
        self.a=a
        self.b=b
    #instance method
    def show(self):
            print("Marks in python= ", self.a)
            print("Marks in python lab= ", self.b)
    #classmethod tells this method is a specific clas method
    #it won't worrrk without @class... because instutution variable is used
    @classmethod
    #self is needed to tell it is not a simple func, it is related to class
    def info(self):
            print("class belongs to ", self.institution)
    #to differ this, @staticmethod is used
    @staticmethod
    def about():
        print("This will be same for each instance")

s1=student(12, 10)
s2=student(13, 11)
s3=student(14, 9)
s1.show()
s2.show()
s3.show()
s1.info()
print(student.institution)
