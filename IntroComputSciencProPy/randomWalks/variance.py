def variance(x):
    """Assumes that x is a list of number.
    Returns the standard deviation of c"""
    mean = sum(x)/len(x)
    tot = 0.0
    for i in x:
        tot += (i-mean)**2
    return tot/len(x)

def stdDev(x):
    """x is a list of numbers"""
    return variance(x)**0.5

