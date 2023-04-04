def isPalindrome(s):
    """Assume s is a str
    return True if letter in s form a palindrome
    ;False otherwise. Non-letters and capitalization are ignored"""
    def toChars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c  in 'abcdefghijklmopqrstuvwxyz':
                letters = letters+c
        return letters
    def isPal(s):
        if len(s)<=1:
            return True
        else:
            return s[0]==s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))


def testIsPalindrome():
    print('Try dogGod')
    print(isPalindrome('dogGod'))
    print('Try dogGood')
    print(isPalindrome('dogGood'))

testIsPalindrome()
