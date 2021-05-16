# # adjecency_list={
# #     "A" : ['B','C','D'],
# #     "B" : ['A','C'],
# #     'C' : ['B','D'],
# # }

# # print(adjecency_list["B"])

# class graph:
#     def __init__(self,x,is_directed=True):
#         self.nodes=x
#         self.adjecency_list={}
#         self.is_directed=is_directed
    
#         for node in self.nodes:
#             self.adjecency_list[node]=[]
    
#     def prin(self):
#         for node in self.nodes:
#             print(node,">",self.adjecency_list[node])

#     def insertedge(self,u,v):
#         self.adjecency_list[u].append(v)
#         if not self.is_directed:
#             self.adjecency_list[v].append(u)
    
#     def deleteedge(self,u,v):
#         self.adjecency_list[u].remove(v)
#         if not self.is_directed:
#             self.adjecency_list[v].remove(u)
    
#     def degree(self,u):
#         return len(self.adjecency_list[u])


# n=["A","B","C","D"]
# gr=graph(n,is_directed=False)
# gr.prin()
# print("Inserting Edges in the Adjacency List in 3..2..1.....!")
# gr.insertedge("A","B")
# gr.insertedge("C","D")
# gr.insertedge("A","C")
# gr.insertedge("A","D")
# gr.prin()
# print("Deleting and edge in 3..2..1...!")
# gr.deleteedge("A","B")
# gr.prin()
# print("Edge Deleted Successfully..!")
# print(gr.degree("A"))
class graph:
    def __init__(self,x,directed=True):
        self.node=x
        self.adj_list={}
        self.directed=directed
        for nodes in self.node:
            self.adj_list[nodes]=[]
        self.arr=[]
    
    def prin(self):
        for nodes in self.node:
            print(nodes,">",self.adj_list[nodes])
    
    def insertedge(self,u,v):
        self.adj_list[u].append(v)
        if self.directed == False:
            self.adj_list[v].append(u)

    def bfs(self,x):
        # temp=x
        # self.arr.append(x)
        # self.arr.append(self.adj_list[x])
        # for nodes in self.node[1:]:
        #     if nodes not in self.arr:
        #         self.arr.append(nodes)
        #     for j in self.adj_list[nodes]:
        #         if j not in self.arr:
        #             self.arr.append(j)
        # return self.arr
        for nodes in self.node:
            if nodes not in self.arr:
                self.arr.append(nodes)
            for j in self.adj_list[nodes]:
                if j not in self.arr:
                    self.arr.append(j)
        return self.arr
        # for nodes in self.node:  
        #     if len(self.adj_list[nodes])!=0:
        #         self.arr.append(nodes)
        #         self.arr.append(" ".join(str(x)for x in self.adj_list[nodes]))
        # return " ".join(self.arr)
n=["A","B","C","D","E","F"]
g=graph(n,directed=False)
g.prin()
# g.insertedge("A",'B')
# g.insertedge("A","C")
# g.insertedge("C","D")
# g.insertedge("B","D")
# g.insertedge("C","B")
g.insertedge("A",'B')
g.insertedge("A","C")
g.insertedge("C","E")
g.insertedge("B","D")
g.insertedge("D","F")
g.insertedge("A","F")
g.insertedge("E","F")
g.prin()

print(g.bfs("A"))