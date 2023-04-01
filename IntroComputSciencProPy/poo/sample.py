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
    #No apropiado para no estar agregando mas sublaxses
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

class Grades(object):
    def __init__(self):
        """Create empty grade book"""
        self.students = []
        self.grades ={}
        self.isSorted = True

    def addStudent(self, student):
        """Assumes : studen is of tupe Studemnt
        add studento to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()]=[]
        self.isSorted = False

    def addGrade(self, student,grade):
        """Assuemes : grade is floar
        Add grade to the list of grades for student"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in maping')
    def getGrades(self, student):
        """Return a lsit of grades for student"""
        try:#Retorna una copia de la lista
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('Student nor in  mapping')
    def getStudents(self):
        """Return a sorted list of the students in the grade book """
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        for s in self.students:
            yield s
        #return self.students[:]

def gradeReport(course):
    """Assumes  course is of type Grades"""
    report = ''
    for s in course.getStudents():
        tot=0.0
        numGrades=0
        for g in course.getGrades(s):
            tot +=g
            numGrades +=1
        try:
            average = tot/numGrades
            report = report +'\n'+str(s)+'\'s mean grade is '+str(average)
        except:
            report = report +'\n'+str(s)+'has no grades'
    return report

class infoHiding(object):
    def __init__(self):
        self.visible = 'Look at me'
        self.__alsoVisible__ = 'Look at me too'
        self.__invisible = 'Don\' look at me directly'
    def printVisible(self):
        print(self.visible)

    def printInvisible(self):
        print(self.__invisible)

    def __printInvisible(self):
        print(self.__invisible)

    def __printInvisible__(self):
        print(self.__invisible)


book = Grades()
book.addStudent(Grad('Julie'))
book.addStudent(Grad('Charlie'))
for s in book.getStudents():
    print(s)
"""
test = infoHiding()
test.printInvisible()
test.__printInvisible__()
test.__printInvisible()
"""
"""
ug1 = UG('Jave Doe', 2014)
ug2 = UG('John  Doe', 2015)
ug3 = UG('David Henry', 2003)
g1 = Grad('Billy Buckner')
g2 = Grad('Bucky F.  Dent')
sixHundred = Grades()
sixHundred.addStudent(ug1)
sixHundred.addStudent(ug2)
sixHundred.addStudent(g1)
sixHundred.addStudent(g2)

for s in sixHundred.getStudents():
    sixHundred.addGrade(s,75)

sixHundred.addGrade(g1,25)
sixHundred.addGrade(g2,100)
sixHundred.addStudent(ug3)
print(gradeReport(sixHundred))
"""
























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
