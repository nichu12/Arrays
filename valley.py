path=12
steps='DDUUDDUDUUUD'
cnt=0
valley=0


for i in steps :
    if i == 'U':
        valley = valley + 1
        if valley == 0:
            cnt= cnt + 1
    elif i == 'D':
        valley = valley - 1

print(cnt)



