# class Student:
#     larki = "bmw"
#     bmw="mansi"
#     ola_ka_bhara= 10000
#     pass


# mk=Student()
# pkc=Student()

# mk.name="MK"
# mk.transport=Student.ola_ka_bhara//2
# mk.interest="chumt"

# pkc.name="Chobeeeyyy"
# pkc.larki=Student.larki
# pkc.transport=Student.larki
# pkc.bmw=Student.bmw
# pkc.interest="gulambi"

# # print(mk.name)
# # print(pkc.interest)
# print(mk.__dict__)
# print(pkc.__dict__)


# class Gniot:
#     salary=50000
#     fees=100000
#     def printDetails(self):
#         return f"Name of Teacher is {self.name} and his salary is {self.salary}"
#     def printStudent(self):
#         return f"Name of Student is {self.name} and his fees is {self.fee}"
    

# teacher1=Gniot() #object or insatance
# student1=Gniot()
# teacher2=Gniot() 
# student2=Gniot()


# teacher1.name="Deepak Sir"
# teacher2.name="Manoj Sir"
# teacher1.salary=Gniot.salary
# teacher2.salary=Gniot.salary

# student1.name="MK"
# student2.name="Amit"
# student1.fee=Gniot.fees
# student2.fee=Gniot.fees

# print(teacher1.__dict__)
# print(student2.__dict__)
# print(teacher1.printDetails())
# print(student2.printStudent())


class boy:
    def __init__(self,aname,arole,aage):
        self.name=aname
        self.role=arole
        self.age=aage

    @classmethod
    def clssmethod(cls,s):
        return cls(*s.split(" "))

    def printd(self):
        return f"My name is {self.name},my role is {self.role} and my age is {self.age}"

mk=boy.clssmethod(input())
print(mk.age)
print(mk.printd())
