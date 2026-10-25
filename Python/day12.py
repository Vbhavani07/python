List=[[1,2],[2,3],[1,2],[5,6]]
updated=list(set(tuple(i) for i in List))
res=(List(i) for i in updated)
print(res)
