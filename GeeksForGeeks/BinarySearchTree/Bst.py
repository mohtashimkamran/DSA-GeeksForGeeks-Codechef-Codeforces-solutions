# class Node:
#     def __init__(self,x):
#         self.root=x;self.right=None;self.left=None

# class Bst:
#     def Searching(self,head,x):
#         if head==None:
#             print(False)
#         else:
#             if head.root == x:
#                 print(True)
#             elif(head.root<x):
#                 self.Searching(head.right,x)
#             else:
#                 self.Searching(head.left,x)
#     def iterativeSearch(self,head,x):
#         while(head !=None):
#             if head.root==x:
#                 return True
#             elif(head.root<x):
#                 head = head.right
#             else:
#                 head = head.left
#         return False

# n1=Node(10)
# n2=Node(20)
# n3=Node(5)
# n4=Node(7)
# n5=Node(3)
# n6=Node(15)
# n7=Node(25)
# n1.left=n3
# n1.right=n2 
# n2.left=n6
# n2.right=n7
# n3.left=n5
# n3.right=n4           

# bt=Bst()
# # print(bt.Searching(n1,15))
# # bt.Searching(n1,26)
# print(bt.iterativeSearch(n1,7))

class Node:
    def __init__(self,x):
        self.root=x
        self.left=None
        self.right=None
    
class Tree:
    def insertion(self,head,x):
        if head ==None:
            return Node(x)
        elif(x>head.root):
            head.right=self.insertion(head.right,x)
        elif(x<head.root):
            head.left=self.insertion(head.left,x)
        return head          
    
    def iterativeinsert(self,head,x):
        if head == None:
            return Node(x)
        temp=head
        while(True):
            if temp.root<x and temp.right==None:
                temp.right=Node(x)
                return head
            elif temp.root>x and temp.left==None:
                temp.left=Node(x)
                return head
            elif temp.root<x:
                temp=temp.right
            elif(temp.root>x):
                temp=temp.left
        # return head
    def successor(self,head):
        temp = head.right
        while(temp!= None and temp.left!=None):
            temp=temp.left
        return temp
    def deletion(self,head,x):
        if head==None:
            return
        elif(head.root>x):
            head.left=self.deletion(head.left,x)
        elif(head.root<x):
            head.right=self.deletion(head.right,x)
        else:
            if head.left==None:
                return head.right
            elif(head.right==None):
                return head.left
            else:
                h=self.successor(head)
                head.root=h.root
                head.right=self.deletion(head.right,h)
        return head   

    def inorder(self,head):
        if head != None:
            self.inorder(head.left)
            print(head.root,end=">")
            self.inorder(head.right)
            
    def floor(self,head,x):
        res=0
        if head==None:
            return
        if head.root==x:
            return head
        elif (head.root>x):
            head=head.left
        else:
            res=head.root
            head=head.right
        return res

tt=Tree()
head=None
for i in range(5):
    n=int(input())
    head=tt.insertion(head,n)

tt.inorder(head)
print()
# h=None
# for i in range(10):
#     h=tt.iterativeinsert(h,i)

# tt.inorder(h)
t=tt.deletion(head,0)
tt.inorder(t)
print()
print(tt.floor(t,5))