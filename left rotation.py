l=[1,2,3,4,5]
n=4
res=[]

for i in range(n):
    l.append(l[i])
for i in range(n):
    del l[0]
print(l)