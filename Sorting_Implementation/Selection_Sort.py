import time


def Selection_Sort(arr):
    copy = arr[:]
    start = time.perf_counter()
    for i in range(0, len(copy)):
        min_index = i
        for j in range(i+1, len(copy)):
            if copy[j] < copy[min_index]:
                min_index = j
        copy[i], copy[min_index] = copy[min_index], copy[i]
    end = time.perf_counter()
    return copy, end - start
