#implementation of linked list in python


# class Node:
#     def __init__(self,data):
#         self.head=data
#         self.next=None

# n1=Node(34)
# n2=Node(65)
# n3=Node(70)

# n1.next=n2
# n2.next=n3

# print(n1.head)

# print(n2.head)

# print(n3.head)

# print(n1.next.next.head)


#traversing through each element of linked list

# class Node:
#     def __init__(self,data):
#         self.head=data
#         self.next=None

# n1=Node(34)
# n2=Node(65)
# n3=Node(70)

# n1.next=n2
# n2.next=n3



# temp=n1
# count=1
# while(temp.next != None):
#     print(temp.head,end="|   |")
#     count+=1
#     temp=temp.next
# print(temp.head)
# print(count)

#insertion at the beginning of singly linked list

# class Node:
#     def __init__(self,data):
#         self.head=data
#         self.next=None


# n1=Node(10)
# n2=Node(15)
# n3=Node(20)

# n1.next=n2
# n2.next=n3

# # print(n1.head)
# # print(n1.next.head)

# n0=Node(5)
# n0.next=n1
# # print(n0.head)
# # print(n0.next.next.next.head)

# temp=n0

# while(temp.next!=None):
#     print(temp.head)
#     temp=temp.next
# print(temp.head)

#delete First node of a singly linked list

# class node:
#     def __init__(self,data):
#         self.head=data
#         self.next=None

# n1=node(10)
# n2=node(20)
# n3=node(40)
# n4=node(50)

# n1.next=n2
# n2.next=n3
# n3.next=n4

#linked list ka baap

# class node:
#     def __init__(self,data):
#         self.head=data
#         self.next=None


# class linkedlist:
#     def printLinked(self,first):
#         temp=first
#         while(temp.next!=None):
#             print(temp.head)
#             temp=temp.next
#         print(temp.head)
    
#     def insertion_after_a_node(self,first,position,element):
#         n=node(element)
#         temp=first
#         while(temp.head!=position):
#             temp=temp.next
#         nn=temp.next
#         temp.next=n
#         n.next=nn
    
#     def deleteion(self,first,previous):
#         try:
#             temp=first
#             while(temp.head!=previous):
#                 temp=temp.next
            
#             x=temp.next
#             y=x.next
#             temp.next=y
#         except Exception:
#             print("Node Not Found",previous)

#     def searching(self,first,element):
#         temp=first
#         count=1
#         while(temp.head!=element):
#             count+=1
#             temp=temp.next
#         print(count)
# ll=linkedlist()


# n1=node(10)
# n2=node(20)
# n3=node(40)
# n4=node(50)

# n1.next=n2
# n2.next=n3
# n3.next=n4


# # ll.printLinked(n1)

# ll.insertion_after_a_node(n1,20,60)
# ll.printLinked(n1)

# # ll.deleteion(n1,100)

# # ll.printLinked(n1)

# ll.searching(n1,60)

# class Node:
#     def __init__(self,data):
#         self.head=data
#         self.prev=None
#         self.next=None

# n1=Node(10)
# n2=Node(20)
# n3=Node(30)
# n4=Node(40)

# n1.next=n2
# n2.prev=n1
# n2.next=n3
# n3.prev=n2
# n3.next=n4
# n4.prev=n3

# temp=n2
# print(n1.prev)
# print(n1.head)
# while(temp.next!=None):
#     print(temp.head)
#     print(temp.prev.head)
#     temp=temp.next
# print(temp.head)
# print(temp.prev.head)
# print(temp.next)

class Node:
    def __init__(self,x):
        self.head=x
        self.next=None
    
class Linked:
    def prin(self,head):
        temp=head
        while(temp!=None):
            print(temp.head,end="||")
            temp=temp.next
        # print(temp.head)

    def inser(self,head,data):
        if head == None:
            return Node(data)
        else:
            # a=head.next
            # head.next=data
            # data.next=a
            # return head
            temp=head
            while(temp.next!=None):
                temp=temp.next
            temp.next=Node(data)
            return head

ll=Linked()
n=int(input("sixze="))
n1=None
# n1=Node(10)
# ll.prin(n1)
for i in range(n):
    x=int(input())
    n1=ll.inser(n1,x)
ll.prin(n1)