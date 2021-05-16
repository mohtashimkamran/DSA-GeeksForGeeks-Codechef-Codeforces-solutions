#convert tree to doubly linked list

# class Node:
#     def __init__(self,x):
#         self.root=x
#         self.left=None
#         self.right=None

# class Linked:
#     def __init__(self,x):
#         self.head=x
#         self.next=None
#         self.prev=None
# class Doubly:
#     def insertion(self,head,x):
#         if head == None:
#             return Linked(x)
#         temp= head
#         while(temp.next!=None):
#             temp=temp.next
#         temp.next=Linked(x)
#         Linked(x).prev=temp
#         return head
#     def printL(self,head):
#         temp=head
#         while(temp!=None):
#             print(temp.head,end=">")
#             temp=temp.next
# class Tree:
#     arr=[]
    # def inorder(self,head):
    #     if head==None:
    #         return 
    #     self.inorder(head.left)
    #     # print(head.root,end=">")
    #     self.arr.append(head.root)
    #     self.inorder(head.right)
    #     return self.arr

# tt=Tree()
# n1=Node(10)
# n2=Node(5)
# n3=Node(5)
# n4=Node(2)
# n5=Node(3)
# n6=Node(38)
# n7=Node(2)
# n1.left=n2
# n1.right=n3
# n2.left=n4
# n2.right=n5
# n3.left=n6
# n3.right=n7
# # print(tt.inorder(n1))

# ll=Doubly()
# head=None
# arr=tt.inorder(n1)
# for i in range(7):
#     head = ll.insertion(head,arr[i])
# ll.printL(head)
# # print(head.next.head)



# class Node:
#     def __init__(self,x):
#         self.root=x
#         self.left=None
#         self.right=None


# class Tree:
#     preIndex=0
#     def construct(self,ino,pre,low,high):
#         if high<low:
#             return
#         inIndex=low
#         x=Node(pre[self.preIndex])
#         self.preIndex+=1
#         for i in range(low,high+1):
#             if ino[i]==x.root:
#                 inIndex=i
#                 break
        
#         x.left=self.construct(ino,pre,low,inIndex-1)
#         x.right=self.construct(ino,pre,inIndex+1,high)
#         return x
#     def inorder(self,head):
#         # if head==None:
#         #     return 
#         if(head!=None):
#             self.inorder(head.left)
#             print(head.root,end=">")
#             self.inorder(head.right)

# ino=[20,10,40,30,50]
# pre=[10,20,30,40,50]

# tt=Tree()
# x=tt.construct(ino,pre,0,len(ino)-1)
# tt.inorder(x)


class Node:
    def __init__(self,x):
        self.root=x
        self.right=None
        self.left=None


n1=Node(10)
n2=Node(5)
n3=Node(5)
n4=Node(2)
n5=Node(3)
n6=Node(38)
n7=Node(2)
n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5
n3.left=n6
n3.right=n7
def spiral(head):
    a1=[]
    a2=[]
    if head == None:
        return 
    a1.append(head)
    while(len(a1)!=0 or len(a2)!=0):
        while(len(a1)!=0):
            temp=a1[-1]
            a1.pop()
            print(temp.root,end=">")
            if temp.right!=None:
                a2.append(temp.right)
            if (temp.left!=None):
                a2.append(temp.left)
        while(len(a2)!=0):
            temp=a2[-1]
            a2.pop()
            print(temp.root,end=">")
            if temp.right!=None:
                a1.append(temp.right)
            if (temp.left!=None):
                a1.append(temp.left)

spiral(n1)