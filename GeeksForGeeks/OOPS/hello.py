class D704:
    rent=16000
    def __init__(self,aname,arole,arent,ainterset):
        self.name=aname
        self.role=arole
        self.rent=arent
        self.interest=ainterset

    def printd(self):
        return f" Name is-{self.name}\n Role is-{self.role}\n Rent is-{self.rent}\n His Interest is {self.interest}"

ujju=D704("JUUJ","Majnu Bhaiya",(16000/3)/3,"Gand marvana")
ankit=D704("Ankit Cha","Ankit Gandvi",(16000/3)/3,"Chumt ka bhookha")
pkc=D704("ChobeyJi","Jeetu",(16000//3)//2,"Bmw")
amit=D704("Amit JI","Delhi ka hai aisa ye kahta hai",16000//3,"Sex Worker")
Mk=D704("Mk","Pavitra Balak",(16000//3)//2,"Gand maarna")
    
print(ujju.printd())
print("\n")
print(ankit.printd())
print("\n")
print(pkc.printd())
print("\n")
print(amit.printd())
print("\n")
print(Mk.printd())
