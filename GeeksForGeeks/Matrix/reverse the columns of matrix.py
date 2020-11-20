# reverse the columns of matrix

row=int(input())
column=int(input())
mat=[]
for i in range(row):
    x=[]
    for j in range(column):
        x.append(int(input()))
    mat.append(x)
print(mat)

for i in range(0,row):
    start=0
    end=row-1
    while(start<end):
        mat[i][start],mat[i][end]=mat[i][end],mat[i][start]

        start+=1
        end-=1

print(mat)
