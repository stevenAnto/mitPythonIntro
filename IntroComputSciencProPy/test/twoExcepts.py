def getGrades(fname):
    try:
        gradesFile = open(fname,'r')
    except IOError:
        raise ValueError('getGrades could not open'+fname)

    grades =[]
    for line in gradesFile:
        print(line)
        print(float(line))
        try:
            grades.append(float(line))
        except:
            raise ValueError('Unable to conver line to float')
    print('salio for')
    return grades

try:
    grades = getGrades('grades.txt')
    grades.sort()
    median = grades[len(grades)//2]
    print('Median grade is', median)
except ValueError as errorMsg:
    print('Whoops',errorMsg)
