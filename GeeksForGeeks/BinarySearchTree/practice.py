class node:
    def __init__(self,val):
        self.root=val
        self.left=None
        self.right=None
class operation:
    def insertt(self,head,x):
        if head==None:
            return node(x)
        else:
            if x>head.root:
                head.right = self.insertt(head.right,x)
            else:
                head.left = self.insertt(head.left,x)
        return head
    def inorder(self,head):
        if head != None:
            self.inorder(head.left)
            print(head.root,end=">")
            self.inorder(head.right)

tt=operation()
n1=None
for i in range(10):
    n1=tt.insertt(n1,i)

tt.inorder(n1)
