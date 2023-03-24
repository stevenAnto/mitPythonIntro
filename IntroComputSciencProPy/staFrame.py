def f(x):
    def g():
        x = 'abs'
        print ('x=',x)
    def h():
        z = x
        print('z=',z)
    x=x+1
    print('x=',x)
    h()
    g()
    print ('x=',x)
    return g

x= 3
z=f(x)
print ('1x=',x)
print ('2z=',z)
z()
