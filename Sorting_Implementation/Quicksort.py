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

def quickSort(arr, l, h, count = True):
    passes = 0
    if(l<h and passes<count):
        j = partition(arr, l, h)
        quickSort(arr, l, j-1)
        quickSort(arr, j+1, h)
        passes += 1

def timedQuickSort(arr):
    start = time.perf_counter()
    quickSort(arr, 0, len(arr)-1)
    end = time.perf_counter()
    return arr, end - start

def kthElement(arr, k):
    quickSort(arr, 0, len(arr)-1, k)
    return arr[k-1]