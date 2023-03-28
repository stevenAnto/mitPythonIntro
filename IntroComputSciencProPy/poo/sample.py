import datetime

class Person(object):
    
    def __init__(self,name):
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name
        self.birthday = None

    def getName(self):
        return self.name

    def getLastName(self):
        return self.lastName

    def setBirthday(self, birthdate):
        """Assumes birthdate is of type datetime.date """
        self.birthday = birthdate

    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today()-self.birthday).days

    def __lt__(self,other):
        
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName<other.lastName

    def __str__(self):
        return self.name

class MITPerson(Person):
    nextIdNum = 0

    def __init__(self, name):
        Person.__init__(self,name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum +=1

    def getIdNum(self):
        return self.idNum

    def __lt__(self,other):
        return self.idNum < other.idNum
    def isStudent(self):
        return isinstance(self,Student)
    #def isStudent(self):
        #return type(self)==Grad or type(self)==UG


class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self,name,classYear):
        MITPerson.__init__(self,name)
        self.year = classYear
    def getClass(self):
        return self.year

class Grad(Student):
    pass

class TransferStudent(Student):
    def __init__(self,name,fromSchool):
        MITPerson.__init__(self,name)
        self.fromSchool ==fromSchool

p5 = Grad('Buzz Aldrin')
p6 = UG('Buzz Aldrin',1984)
print(p5,'is a graduate student is',type(p5)==Grad)
print(p5,'is a undergraduate student is',type(p5)==UG)

me =  Person('Michael Guttag ')
him = Person ('Barack Hussein Obama')
her = Person('Madonna')
him.setBirthday(datetime.date(1961,8,4))
her.setBirthday(datetime.date(1958,8,16))
#print(him.getName(),'is',him.getAge(),'days old')
"""pList = [me,him,her]
for p in pList:
    print(p)
    
pList.sort()
for p in pList:
    print(p)"""
#p1 =MITPerson('Mark Guttag')
#p1.nextIdNum = 5
print(MITPerson.nextIdNum)
#p2 =MITPerson('Billy Bob Beaver')
p3 =MITPerson('Billy Bob Beaver')
#p4 =Person('Billy Bob Beaver')
#print(str(p1)+'\'s id number is '+str(p1.getIdNum()))
#print(p1<p2)
#print(p3<p2)
#print(p4<p1)
