total=0
number=''
numberInt=0
for c in '12,13,10,4':
    if c!=',':
        number = number+c
    elif c==',':
        numberInt=int(number)
        number=''
        total = total+numberInt
    print(numberInt)
    print('el total ',total)
print(total)
