matrix=[[1,2,3],[4,5,6],[7,8,9]]
flat=[]
for i in matrix:
    for j in i:
        flat.append(j)
print(flat)