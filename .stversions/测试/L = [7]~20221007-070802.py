L = [7]
min = None
max = None
if L :
    if len(L) == 1 :
        min = max = L
    else:
        min = max = 0
        for i in L:
            if min > i :
                min = i
            if max < i :
                max = i
print(min,max)