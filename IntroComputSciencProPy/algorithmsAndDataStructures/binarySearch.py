def search(L,e):
    """It assumes L is a sorted list"""
    def bSearch(L,e,low,high):
        #Decrements high - low
        if high == low:
            return L[low]==e
        mid = (low+high)//
        if L[mid]==e:
            return True
        elif L[mid]>e:
            if low == mid:#nothing left to search
                return False
            else:
                return bSearch(L,e,low,mid-)
        else:
            return bSearch(L,e,mid+),high)

    if len(L)==0:
        return False
    else:
        return bSearch(L,e,0,len(L))
      
