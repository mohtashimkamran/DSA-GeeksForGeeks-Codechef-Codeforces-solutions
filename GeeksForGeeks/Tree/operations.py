class Node:
    def __init__(self,x):
        self.root=x;self.left=None;self.right=None


class Tree:
    res=0
    index=0
    def height(self,head):
        if head == None:
            return 0
        return max (self.height(head.left),self.height(head.right))+1

    def diameter(self,head):
        if head == None:
            return 0
        h1 = 1+self.height(head.left)+self.height(head.right)

        h2=self.diameter(head.left)
        h3=self.diameter(head.right)
        
        return max(h1,max(h2,h3))

    def efficientdiameter(self,head):
        
        if head == None:
            return 0
        lh=self.efficientdiameter(head.left)
        rh=self.efficientdiameter(head.right)
        self.res=max(self.res,lh+1+rh)
        
        return 1+max(lh,rh)

    def lowestcommonancestor(self,head,x,y):
        if head==None:
            return None
        if head.root==x or head.root==y:
            return head
        
        lca1=self.lowestcommonancestor(head.left,x,y)
        lca2=self.lowestcommonancestor(head.right,x,y)
    
        if lca1!=None and lca2!=None:
            return head
        if lca1 !=None:
            return lca1
        else:
            return lca2
    def countnode(self,head):
        if head == None:
            return 0
        else:
            return 1 + self.countnode(head.left) + self.countnode(head.right)
        
    def serialization(self,head,arr):
        if head == None:
            arr.append(-1)
        else:
            arr.append(head.root)
            self.serialization(head.left,arr)
            self.serialization(head.right,arr)
    
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
        
        return head.root


tt=Tree()

n1=Node(10)
n2=Node(5)
n3=Node(5)
n4=Node(2)
n5=Node(3)
n6=Node(38)
n7=Node(22)
n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5
n3.left=n6
n3.right=n7

print(tt.height(n1))
print(tt.diameter(n1))
tt.efficientdiameter(n1)
print(tt.res)
x=tt.lowestcommonancestor(n1,5,38)
print(x.root)

print(tt.countnode(n1))

arr=[]
tt.serialization(n1,arr)
print(arr)

print(tt.deserialize(arr))