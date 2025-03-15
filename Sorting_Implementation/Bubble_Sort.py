import time


def Bubble_Sort(arr):
    copy = arr[:]
    start = time.perf_counter()
    for i in range(0, len(copy)):
        is_sorted = True
        for j in range(0, len(copy) - 1 - i):
            if (copy[j] > copy[j+1]):
                is_sorted = False
                copy[j], copy[j+1] = copy[j+1], copy[j]
        if is_sorted == True:
            break
    end = time.perf_counter()
    return copy, end - start
