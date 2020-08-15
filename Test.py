arr = [5, 3, 4, 1, 2]


def select():
    global arr
    for i in range(len(arr) - 1, -1, -1):
        imin = 0
        print(arr)
        for j in range(1, i + 1):
            if arr[imin] < arr[j]:
                imin = j
        arr[i], arr[imin] = arr[imin], arr[i]
        print(arr)


def bubble_sort():
    count = 0
    for i in range(len(arr) - 1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(arr)
        count += 1
    return count


print("Sorted:")
# print(select())
print(bubble_sort())
