def sumDigits(s):
    """Assumes s is a string
    Return the sum of the decimal digits in s
    For example, if s is 'a2b3c' it returns 5"""
    suma =0
    for c in s:
        try:
            suma = suma + int(c)
        except ValueError:
            print('No es un entero')
    return suma

def testSuma(s):
    print(sumDigits(s))

testSuma('a2b3c')
            




