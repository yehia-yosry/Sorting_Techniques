import time
import random


def partition(array, low, high):
    index = random.randint(low, high)
    array[index], array[low] = array[low], array[index]
    pivot = array[low]
    leftwall = low+1
    for i in range(low+1, high+1):
        if array[i] < pivot:
            array[i], array[leftwall] = array[leftwall], array[i]
            leftwall += 1
    array[leftwall-1], array[low] = array[low], array[leftwall-1]
    return leftwall-1

def quickSort(arr, l, h):
    if(l<h):
        j = partition(arr, l, h)
        quickSort(arr, l, j-1)
        quickSort(arr, j+1, h)

def timedQuickSort(arr):
    start = time.perf_counter()
    quickSort(arr, 0, len(arr)-1)
    end = time.perf_counter()
    return arr, end - start

def kthElement(arr, k, low, high):
    index = partition(arr, low, high)
    if(index == k):
        return arr[index]
    elif (index < k):
        return kthElement(arr, k, low, index-1)
    else:
        return kthElement(arr, k, index+1, high)

