class IntSet(object):
    """An intSet is a set of integers"""
    #Information about the implementation(not the abstraction)
    #Value of the set is represented by a list of ints, self.vals
    #Each int in the set occrus in self.vals exactly one
    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []
    def insert(self,e):
        """Assumes e is an integer and inserts e into self"""
        if e not in self.vals:
            self.vals.append(e)

    def member(self,e):
        return e in self.vals

    def remove(self,e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e)+'nor found')
    def getMembers(self):
        return self.vals[:]
    def __str__(self):
        result =''
        for e in self.vals:
            result = result +str(e)+','
        return '{'+result[:-1]+"}"#-1 omits las coma

s= IntSet()
s.insert(3)
print(s.member(3))
print(s.getMembers())
