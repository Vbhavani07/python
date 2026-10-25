s=input()
l=[]
k=[]
c=0
for i in s:
    if i not in l:
        l.append(i)
        c+=1
print("Different Species:",c)
for i in l:
  a=s.count(i)
  k.append(a)
min_count=min(k)
min_char=l[k.index(min_count)]
print("Most Commmon:",i,max(k))
print("Least Common:",min_char,min_count)
print("Frequency species:")
for i in l:
   print(i,s.count(i))

