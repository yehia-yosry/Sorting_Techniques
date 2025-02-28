import time
def insertion_sort(arr):
    start = time.perf_counter()
    for i in range(1, len(arr), 1):
        value = arr[i]
        pos = i
        for j in range(i-1, -1, -1):
            if arr[j] > value:
                arr[j+1] = arr[j]
                pos = j
            else:
                break
        arr[pos] = value
    end = time.perf_counter()
    return arr, end - start