import time
def bubble_sort(arr):
    start = time.perf_counter()
    for i in range(0, len(arr)):
        is_sorted = True
        for j in range(0, len(arr) - 1 - i):
            if (arr[j] > arr[j+1]):
                is_sorted = False
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if is_sorted == True:
            break
    end = time.perf_counter()
    return arr, end - start