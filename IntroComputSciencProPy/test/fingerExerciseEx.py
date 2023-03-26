def findAnEven(L):
    """Assumes L i s a list of integers
    Returns the first even number in L
    Raises ValueError if L does not contain even number"""
    for i in L:
         if i%2!=0:
            return i
    raise ValueError('does not contain even number')

print(findAnEven([2,4,3,6]))
