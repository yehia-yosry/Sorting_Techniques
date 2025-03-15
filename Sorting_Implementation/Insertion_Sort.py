import time


def Insertion_Sort(arr):
    copy = arr[:]
    start = time.perf_counter()
    for i in range(1, len(copy), 1):
        value = copy[i]
        pos = i
        for j in range(i-1, -1, -1):
            if copy[j] > value:
                copy[j+1] = copy[j]
                pos = j
            else:
                break
        copy[pos] = value
    end = time.perf_counter()
    return copy, end - start
