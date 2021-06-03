
c=[0,0,0,1,0,0]
n=len(c)
c.append(1)
jump = 0
i = 0
while(i < (n-2)):
    if c[i] == c[i + 2]:
        jump = jump + 1
        i = i + 2
    elif c[i] == c[i + 1]:
        jump = jump + 1
        i = i + 1
    else:
        break
print(jump)