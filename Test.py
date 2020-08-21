arr = [235, 122, 252, 267, 253, 228, 294, 464, 396, 299, 483, 394, 177, 326, 339, 288, 331, 352, 484, 481, 204, 115, 450, 102, 280, 284, 496, 317, 479, 463, 178, 373, 370, 281, 283, 458, 105, 124, 158, 486]
import time


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


def insertion_sort():
    for i in range(1, len(arr)):
        curr_el = arr[i]
        pos = i
        while curr_el < arr[pos - 1] and pos > 0:
            arr[pos] = arr[pos - 1]
            pos = pos - 1
            print(arr)
        arr[pos] = curr_el
    print(arr)


def partition(arr, low, high):
    i = low
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
    print(arr)


print("Sorted:")
# print(select())
# print(bubble_sort())
# print(insertion_sort())
print(arr)
quickSort(arr, 0, len(arr) - 1)
