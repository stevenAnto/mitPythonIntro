def selSort(L):
    "L is a list of elements  that can be  compared using >"

    suffixStart = 0
    while suffixStart != len(L):
        for i in range(suffixStart,len(L)):
            if L[i]<L[suffixStart]:
                #swap
                L[suffixStart],L[i]=L[i],L[suffixStart]
        suffixStart +=1



lists = [5,2,4,6,1,9]
print(lists)
selSort(lists)
print(lists)
