class Node:
    def __init__(self,x):
        self.val=x
        self.next=None
    
class LinkedList:
    def insertion(self,x,head):
        if head==None:
            return Node(x)
        else:
            temp=head
            while temp.next !=None:
                temp=temp.next
            temp.next=Node(x)
        return head
    
    def printlinkedlist(self,head):
        if head:
            temp=head
            while temp !=None:
                print(temp.val,end="-->")
                temp=temp.next

ll=LinkedList()
head=None
for i in range(10):
    head=ll.insertion(i,head)

ll.printlinkedlist(head)