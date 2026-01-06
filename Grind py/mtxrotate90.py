mtx=[[1,2,3],
     [4,5,6],
     [7,8,9]]
# tran=list(zip(*mtx))
# rot=list(row[::-1] for row in tran)
# print(rot)
 
# tran=list(map(list,zip(*mtx)))
# for i in tran:
#     i.reverse()
# mtx[:]=tran    

# print(mtx)

n=len(mtx)
for i in range(n):
    for j in range(i+1,n):
        mtx[i][j],mtx[j][i]=mtx[j][i],mtx[i][j]
for i in range(n):
    mtx[i].reverse()

print(mtx)    