class Node:
    def __init__(self,data):
        self.head=data
        self.next=None
        # self.prev=None
class CircularLinked:
    def printl(self,start):
        temp=start
        while(temp.next!=start):
            print(temp.head,end="|*|")
            temp=temp.next
        print(temp.head,end="|*|")
        print(temp.next.head)
    def insertatbegin(self,position,data):
        x=Node(data)
        y=position.next
        position.next=x
        x.next=y
    
    def deleteL(self,position):
        y=position.next.head
        position.head=y
        position.next=position.next.next

n1=Node(10)
n2=Node(20)
n3=Node(30)

n1.next=n2
n2.next=n3
n3.next=n1

cl=CircularLinked()
cl.insertatbegin(n2,45)
cl.deleteL(n2)
cl.printl(n1)