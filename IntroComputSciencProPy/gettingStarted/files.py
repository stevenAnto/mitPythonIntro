nameHandle = open('kids','w')
for i in range(2):
    name = input('Enter your name ')
    nameHandle.write(name+'\n')

nameHandle.close()

