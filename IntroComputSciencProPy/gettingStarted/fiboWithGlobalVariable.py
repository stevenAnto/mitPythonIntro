def fib(x):
    """
    x an int ?>=0 returns Fibo of x"""
    global numFibCalls
    numFibCalls +=1
    if x ==0 or x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)

def testFib(n):
    for i in range(n+1):
        numFibCalls = 0
        print('fib of ',i,'=',fib(i))
        print('fib called ',numFibCalls,'times')

testFib(8)
