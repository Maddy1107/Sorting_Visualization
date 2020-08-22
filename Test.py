array = [235, 122, 252, 267, 253, 228, 294, 464, 396, 299, 483, 394]


def merge(arr, l, m1, m2, r):
    temp = []
    i = l
    j = m2

    while i <= m1 and j <= r:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= m1:
        temp.append(arr[i])
        i += 1
    while j <= r:
        temp.append(arr[j])
        j += 1
    j = 0
    for i in range(l, r+1):
        arr[i] = temp[j]
        j += 1


def mergeSort(arr, l, r):
    m = (l + r) // 2
    if l < r:
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, m + 1, r)


mergeSort(array, 0, len(array) - 1)
print(array)
