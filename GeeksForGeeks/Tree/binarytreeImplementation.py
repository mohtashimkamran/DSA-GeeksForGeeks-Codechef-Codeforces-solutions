# class Node:
#     def __init__(self,x):
#         self.root=x
#         self.rightchild=None
#         self.leftchild=None

# if __name__ == "__main__":
#     n1=Node(10)
#     n2=Node(20)
#     n3=Node(5)
#     n1.leftchild=n3
#     n1.rightchild=n2

#     print(n1.root)
#     print(n1.leftchild.root)
#     print(n1.rightchild.root)

# class Node:
#     def __init__(self,x):
#         self.root=x
#         self.rightchild=None
#         self.leftchild=None

# class traverse:
#     def inorder(self,head):
#         if head!=None:
#             self.inorder(head.leftchild)
#             print(head.root,end=" > ")
#             self.inorder(head.rightchild)
        
#     def preorder(self,head):
#         if head!=None:
#             print(head.root,end=" > ")
#             self.preorder(head.leftchild)
#             self.preorder(head.rightchild)
    
#     def postorder(self,head):
#         if head!=None:
#             self.postorder(head.leftchild)
#             self.postorder(head.rightchild)
#             print(head.root,end=" > ")
    
#     #return seight of tree
#     def height(self,head):
#         if head == None:
#             return 0
#         else:
#             return max(self.height(head.leftchild),self.height(head.rightchild))+1



# if __name__ == "__main__":
#     n1=Node(10)
#     n2=Node(20)
#     n3=Node(5)
#     n4=Node(25)
#     n5=Node(30)
#     n6=Node(40)
#     n1.leftchild=n3
#     n1.rightchild=n2
#     n2.leftchild=n4
#     n2.rightchild=n5
#     n3.leftchild=n6

#     bt=traverse()
#     bt.inorder(n1)
#     print()
#     bt.preorder(n1)
#     print()
#     bt.postorder(n1)
#     print()

#     print(bt.height(n1))


# class Node:
#     def __init__(self,x):
#         self.root=x
#         self.left=None
#         self.right=None

# class Tree:

#     def height(self,head):
#         if head==None:
#             return 0
#         else:
#             return max(self.height(head.left),self.height(head.right))+1


#     def Nodeatdistancek(self,head,k):
#         if head == None:
#             return
#         if k==0:
#             print(head.root,end=">")
#         else:
#             self.Nodeatdistancek(head.left,k-1)
#             self.Nodeatdistancek(head.right,k-1)


# n1=Node(10)
# n2=Node(20)
# n3=Node(30)
# n4=Node(50)
# n5=Node(60)
# n6=Node(70)
# n1.left=n2
# n2.left=n3
# n2.right=n4
# n1.right=n5
# n4.left=n6

# bt=Tree()
# bt.Nodeatdistancek(n1,3)
# print(bt.height(n1))
# x=bt.height(n1)
# i=0
# while(i!=x):
#     bt.Nodeatdistancek(n1,i)
#     i+=1
#     print()


# class Node:
#     def __init__(self,x):
#         self.root=x
#         self.left=None
#         self.right=None

# class Tree:
#     m=0
#     a=0
#     def inorder(self,head):
#         if head==None:
#             return 
#         self.inorder(head.left)
#         print(head.root,end=">")
#         self.inorder(head.right)
    
#     def postorder(self,head):
#         if head==None:
#             return
#         self.postorder(head.left)
#         self.postorder(head.right)
#         print(head.root,end=">")
    
#     def preorder(self,head):
#         if head==None:
#             return
#         print(head.root,end=">")
#         self.preorder(head.left)
#         self.preorder(head.right)
    
#     def strength(self,head):
#         if head == None:
#             return 0
#         return 1+(self.strength(head.left))+(self.strength(head.right))
    
#     def getmax(self,head):
#         if head!=None:
#             self.m=max(self.m,head.root)
#             self.getmax(head.left)
#             self.getmax(head.right)
#         return self.m
    
#     def childsum(self,head):
#         s=0
#         if head == None:
#             return True
#         if head.left == None and head.right==None:
#             return True
#         if head.left!=None:
#             s+=head.left.root
#         if head.left!=None:
#             s+=head.right.root
#         return ((s == head.root) and (self.childsum(head.left)) and (self.childsum(head.right)))
    
#     def isbalanced(self,head):
        
#         if head==None:
#             return 0
#         lh = self.isbalanced(head.left)
#         if lh==-1:
#             return -1
#         rh=self.isbalanced(head.right)
#         if rh==-1:
#             return -1
#         if abs(lh-rh)>1:
#             return -1
#         else:
#             return max(lh,rh)+1

#     def kthnode(self,head,k):
        
#         if head==None:
#             return 
#         else:
#             if(k==0):
#                 # print(head.root,end=">")
#                 self.a+=1
#             else:
#                 self.kthnode(head.left,k-1)
#                 self.kthnode(head.right,k-1)
#     def height(self,head):
#         if head==None:
#             return 0 
#         else:
#             return max(self.height(head.left),self.height(head.right))+1

#     def maxwidth(self,head):
#         i=1
#         c=0
#         x=self.height(head)
#         while(i!=x):
#             self.kthnode(head,i)
#             c=max(c,self.a)
#             self.a=0
#             i+=1
#         return c
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
# # n1=Node(8)
# # n2=Node(12) 
# # n3=Node(13)
# # n4=Node(14)
# # n5=Node(15)

# # n1.left=n2
# # n1.right=n3
# # n3.left=n4
# # n3.right=n5

# bt=Tree()
# bt.preorder(n1)
# print()
# bt.postorder(n1)
# print()
# bt.inorder(n1)
# print()
# print(bt.strength(n1))

# print(bt.getmax(n1))

# print(bt.childsum(n1))

# print(bt.isbalanced(n1))

# bt.kthnode(n1,2)
# print()
# x=bt.height(n1)
# print(bt.maxwidth(n1))

#width of a binary tree

class Node:
    def __init__(self,x):
        self.root=x;self.left=None;self.right=None
    
class Tree:
    index=0
    def height(self,head):
        if head == None:
            return 0
        return max(self.height(head.left),self.height(head.right))+1
    def diameter(self,head):
        if head==None:
            return 0
        d1=1+self.height(head.left)+self.height(head.right)

        d2=self.diameter(head.left)
        d3=self.diameter(head.right)
        return max(d1,max(d2,d3))

    def serialize(self,head,arr):
        if head == None:
            arr.append(-1)
        else:
            arr.append(head.root)
            self.serialize(head.left,arr)
            self.serialize(head.right,arr)
    def deserialize(self,arr):
        if self.index==len(arr):
            return None
        else:
            value = arr[self.index]
            self.index+=1
            if value == -1:
                return None
            else:
                head = Node(value)
                
                head.left = self.deserialize(arr)
                head.right= self.deserialize(arr)
            return head
    def inorder(self,head):
        if head==None:
            return 
        self.inorder(head.left)
        print(head.root,end=">")
        # self.arr.append(head.root)
        self.inorder(head.right)
        # return self.arr


tr=Tree()

n1=Node(10)
n2=Node(5)
n3=Node(7)
n4=Node(2)
n5=Node(3)
n6=Node(38)
# n7=Node(2)
# n8=Node(11)
n1.left=n2
n1.right=n3
n3.left=n4
n3.right=n5
n4.left=n6
# n3.right=n7
# n7.right=n8

print(tr.height(n1))

print(tr.diameter(n1))

a=[]
tr.serialize(n1,a)
print(a)
head=tr.deserialize(a)
tr.inorder(head)