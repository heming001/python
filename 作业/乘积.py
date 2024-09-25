def mul(L=None,*number):
    sum = 1

    sum = sum * L
    for n in number:
        sum = sum * n
    return sum

print(mul(5,6))
print(mul())