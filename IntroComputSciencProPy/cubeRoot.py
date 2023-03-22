#Find the cube  root of a perfect cube
x=int(input('ingre su numero'))
for ans in range(0,abs(x)+1):
    if ans**3>=abs(x):
        break
# the variable's scoope is out of for
if ans**3!=abs(x):
    print(x,'is not a perfect cub')
else:
    if x<0:
        ans = -ans
    print('cube root of ',x,'is',ans)
