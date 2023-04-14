def myFun(*argv):
    print(len(argv))
    for arg in argv:
        print(arg)


#generator

def shout(test):
    return test.upper()

def whisper(text):
    return text.lower()

def greet(func):
    #storing the function in a variable
    greeting = func("Soy una fucnion")
    print(greeting)

def create_adder(x):
    def adder(y):
        return x+y
    return adder

add_15 = create_adder(15)

print(add_15(10))

