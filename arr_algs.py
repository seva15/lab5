def min_val(arr):
    return min(arr)


def mid_val(arr):
    return sum(arr)/len(arr)

for i in range(1, 4):
    arr = list(map(int, input().split()))
    print('\n', min_val(arr), '\n', mid_val(arr))