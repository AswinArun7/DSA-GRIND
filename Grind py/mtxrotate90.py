mtx=[[1,2,3],
     [4,5,6],
     [7,8,9]]
# tran=list(zip(*mtx))
# rot=list(row[::-1] for row in tran)
# print(rot)
 
tran=list(map(list,zip(*mtx)))
for i in tran:
    i.reverse()

print(tran)    