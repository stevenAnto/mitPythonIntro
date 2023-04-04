monthNumbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5,1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May'}
keys =[]

for e in monthNumbers:
    keys.append(str(e))

print(keys)
keys.sort()
print(keys)
