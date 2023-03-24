
def isIn(str1,str2):
    if str1.find(str2)!=-1 or str2.find(str1)!=-1:
        return True
    else:
        return False

x=input('Ingrese la primera cadea')
y=input('Ingrese la primera cadea')
print(isIn(x,y))

