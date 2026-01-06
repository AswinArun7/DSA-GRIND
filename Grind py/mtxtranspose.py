matrix=[[1,2,3],[5,6,8],[8,1,5]]
# tr_mtx=list(map(list,zip(*matrix)))
# print(tr_mtx)

n=len(matrix)
for i in range(n):
    for j in range(i+1,n):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

print(matrix)