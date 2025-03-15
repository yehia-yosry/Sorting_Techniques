import time


def Selection_Sort(arr):
    start = time.perf_counter()
    for i in range(0, len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    end = time.perf_counter()
    return arr, end - start
