def readInt():
    while True:
        val  =int('Enter a integer')
        try :
            return int(val)
        except ValueError:
            print(val,'is not an integer')

def readVal(valType,requestMsg,errorMsg):
    while True:
        val = input(requestMsg+'')
        try:
            return (valType(val))
        except ValueError:
            print(val, errorMsg)
            val =None

val = readVal(int, 'Enter an integer:','is not an integer')
