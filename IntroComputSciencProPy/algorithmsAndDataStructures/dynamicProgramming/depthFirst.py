import item  as it

def maxVal(toConsider, avail):
    """Assumes toConsider is a list of items, avail is a weight
    Returns a tuple of the total value of a solution to the 0/1 knapsack problem and the items of the solution"""
    if toConsider==[] or avail==0:
        result = (0,())
    elif toConsider[0].getWeight()>avail:

        #como no tomare el primer elemento me muevo hacia la derecha del arbol de decision
        result = maxVal(toConsider[1:],avail)
    else:
        nexItem = toConsider[0]
        #lef branch
        withVal, withToTake = maxVal(toConsider[1:],avail-nexItem.getWeight())
        withVal += nexItem.getValue()
        #right branch
        withoutVale, withoutToTake = maxVal(toConsider[1:],avail)
        if withVal >withoutVale:
            result = (withVal,withToTake+(nexItem,))
        else:
            result= (withoutVale,withoutToTake)
    return result

def smallTest():
    names =['a','b','c','d']
    vals = [6,7,8,9]
    weights = [3,3,2,5]
    Items = []
    for i in range(len(vals)):
        Items.append(it.Item(names[i],vals[i],weights[i]))
    val, taken =maxVal(Items,5)
    for item in taken:
        print(item)
    print('The total value is :', val)


smallTest()
