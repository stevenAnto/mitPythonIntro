def getRatios(vect1,vect2):
    """Assumes : vect1 and vect2 are equal length list of number
    Returns : a list cotaining the meaningful values of vect1[i]/vect2[i]"""

    ratios = []
    for index in range(len(vect1)):
        try:
            ratios.append(vect1[index]/vect2[index])
        except ZeroDivisionError:
            ratios.append(float('nan'))
        except:
            raise ValueError('bad arguments')
    return ratios

try:
    print(getRatios([1.0,2.0,7.0,6.0],[1.0,2.0,0.0,3.0]))
    print(getRatios([],[]))
    print(getRatios([1.0,2.0],[3.0]))
except ValueError as msg:
    print(msg)
