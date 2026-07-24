
                                              #File I/O
def gr8():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=int(input("Enter third number: "))
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    
f=open("greatest.txt","w")
f.write(f"The greatest number is: {gr8()}")
f.close()

                                                #OOPs

class Student():
    age=19
    job="no"
    salary=0
    def __init__(self):
            print("Here is data of student") 
    def getinfo(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Job: {self.job}")
        print(f"Salary: {self.salary}")  

class Faculty():
    age=35
    job="yes"
    salary=50000
    def getinfo(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Job: {self.job}")
        print(f"Salary: {self.salary}")

class Authority():
    position="Teacher"
    age=35
    salary=60000

    def getinfo(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Position: {self.position}")
        print(f"Salary: {self.salary}")
ab=Student()
cd=Faculty()
ef=Authority()
ab.name="Adil"
cd.name="XYZ"
ef.name="ABC"
ef.salary=90000
ab.getinfo()
cd.getinfo()
ef.getinfo()
    