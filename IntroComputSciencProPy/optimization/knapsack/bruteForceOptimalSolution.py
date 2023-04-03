import item as it
import generatioPowerSet
import greedy

def chooseBest(pset, maxWeigth, getVal, getWeight):
    bestVal = 0.0
    bestSet = None
    for items in pset:
        itemsVal = 0.0
        itemsWeight = 0.0
        for item in items:
            itemsVal += getVal(item)
            itemsWeight += getWeight(item)
        if itemsWeight<= maxWeigth and itemsVal> bestVal:
            bestVal = itemsVal
            bestSet = items
    return (bestSet,bestVal)

def testBest(maxWeigth=20):
    items =greedy.buildItems()
    pset = generatioPowerSet.genPowerSet(items)
    taken, val = chooseBest(pset,maxWeigth, it.Item.getValue,it.Item.getWeight)
    print('Total value of items taken is ', val)

    for item in taken:
        print(item)

print('Entro BruteForce')

testBest()

