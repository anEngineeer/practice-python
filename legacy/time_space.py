def squares(arr):
    b = []
    for x in arr:
        b.append(x * x)
    return b

arr = [1, 2, 3, 4, 5]
print(squares(arr))
