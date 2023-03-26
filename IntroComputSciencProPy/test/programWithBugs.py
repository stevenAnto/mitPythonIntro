def isPal(x):
    """Assumes x is a list 
    returns True is the list is a palindrome, False otherwise"""
    temp = x[:]
    temp.reverse()#error
    if temp ==x:
        print(temp,x)
        return True
    else:
        return False

def silly(n):
    """Assumes n is an int>0
    Get n inputs from user
    Print 'yes' if if the sequeda form an palindrome , 'No' otherwise"""

    result =[]
    for i in range(n):
        elem = input('Enter element: ')
        result.append(elem)
    print(result)
    if isPal(result):
        print('Yes')
    else:
        print('No')

silly(2)

