x=0.25
epsilon =0.01
step = epsilon**2
numGuess=0
ans = 0.0
while abs(ans**2-x)>=epsilon and ans*ans<=x:
    ans += step
    numGuess +=1
    print(ans)
print('numGuess = ',numGuess)
if abs(ans**2-x)>=epsilon:
    print('Failes on square root of ',x)
else:
    print(ans,'is close to square roof of',x)
