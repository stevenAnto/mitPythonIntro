"""
1-((n-1)/n)*((n-2)/n)*((n-3)/n)*...*(n-(k-1))/n"""
def collisionProb(n,k):
    prob=1.0
    for i in range(1,k):
        prob=prob*((n-i)/n)
    return 1-prob
print(collisionProb(1000,50))
print(collisionProb(1000,200))

