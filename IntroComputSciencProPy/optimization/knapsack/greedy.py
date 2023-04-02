import item

def greedy(items, maxWeight, keyFunction):
    """Assumes Items a list, masWeight >=0,keyFunction mpas elements of items to numbers"""
    itemsCopy = sorted(items,key = keyFunction,reverse=True)
    result = []
    totalValue, totalWeight = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalWeight + itemsCopy[i].getWeight())<=maxWeight:
            result.append(itemsCopy[i])
            totalWeight += itemsCopy[i].getWeight()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)

def buildItems():
    names = ['clockclock','paiting','radio','vase','book','computer']
    values = [ 175,90,20,50,10,200]
    weights = [10,9,4,2,1,20]
    Items =[]
    for i in range(len(values)):
        Items.append(item.Item(names[i],values[i],weights[i]))

    return Items

def testGreedy(items,maxWeight, keyFunction):
    taken, val = greedy(items, maxWeight,keyFunction)
    print('Total value of items taken is ', val)
    for item in taken:
        print("    ", item)

def testGreedys(maxWeight=20):
    print("entro testGreedy")
    items = buildItems()
    print("Use greedy by value to fill knapssack of size ", maxWeight)
    testGreedy(items,maxWeight,item.value)
    print("\nUse greedy by weight to fill knapssack of size ", maxWeight)
    testGreedy(items,maxWeight,item.weightIverse)
    print("\nUnsa by density ", maxWeight)
    testGreedy(items, maxWeight, item.density)
testGreedys()
