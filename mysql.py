n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
sock = []
res=[]
pairs=0
for i in ar:
    if i not in sock:
        sock.append(i)
for i in sock:
    x=ar.count(i)
    res.append(x)
for i in res:
    pairs = pairs + int(i / 2)
print(pairs)



