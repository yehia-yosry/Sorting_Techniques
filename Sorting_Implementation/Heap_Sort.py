import time

def heapsort(arr):
    start = time.perf_counter()
    buildMaxHeap(arr)
    heap_size = len(arr)
    for i in range(heap_size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heap_size -= 1
        maxHeapify(arr, 0, heap_size)
    end = time.perf_counter()
    return arr, end - start

def buildMaxHeap(arr):
    heap_size = len(arr)
    for i in range(heap_size // 2 - 1, -1, -1):
        maxHeapify(arr, i, heap_size)


def maxHeapify(arr, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2
    if left < heap_size and arr[left] > arr[i]:
        largest = left
    else:
        largest = i
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, largest, heap_size)