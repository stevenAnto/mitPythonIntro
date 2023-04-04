#Sample. Find x such that x**2-24 is within epsilon of 0
epsilon =0.01
k = 24.0
guess = k/2.0 #Es un valor adivinado
counter =0
while(abs(guess*guess-k)>=epsilon):
    guess = guess -(((guess**2)-k)/(2*guess))
    counter +=1
print('counter',counter)
print('square root of ',k,'is about ', guess)

