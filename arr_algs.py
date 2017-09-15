def min_val(arr):
    min_vall = arr[0]
    for i in arr:
        if i<min_vall:
            min_vall=i
    return min_vall


def mid_val(arr):
    summa = 0
    for i in arr:
        summa+=i
    return summa/len(arr)

for i in range(1, 4):
    arr = list(map(int, input().split()))
    print('\n', min_val(arr), '\n', mid_val(arr))