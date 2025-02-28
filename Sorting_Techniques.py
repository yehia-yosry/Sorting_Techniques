import time
import random
import numpy as np
import matplotlib.pyplot as plt # type: ignore


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


def selection_sort(arr):
    start = time.perf_counter()
    for i in range(0, len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    end = time.perf_counter()
    return arr, end - start


def random_array(length):
    arr = []
    for i in range(0, int(length)):
        arr.insert(0, random.randint(0, 100))
    return arr


def time_complexity(input_sizes):
    time_bubble = []
    time_insertion = []
    time_selection = []
    for i in range(0, len(input_sizes)):
        arr = random_array(input_sizes[i])
        time_bubble.append(bubble_sort(arr)[1])
        time_insertion.append(insertion_sort(arr)[1])
        time_selection.append(selection_sort(arr)[1])
    return time_bubble, time_insertion, time_selection


input_sizes = [0, 100, 200, 300, 500]
time_ = time_complexity(input_sizes)
bubble_sort_time = time_[0]
insertion_sort_time = time_[1]
selection_sort_time = time_[2]


plt.plot(input_sizes, bubble_sort_time, marker='o',
         linestyle='-', color='r', label='Bubble Sort')
plt.plot(input_sizes, insertion_sort_time, marker='o',
         linestyle='-', color='g', label='Insertion Sort')
plt.plot(input_sizes, selection_sort_time, marker='o',
         linestyle='-', color='b', label='Selection Sort')

plt.xlabel("Input Size(N)")
plt.ylabel("Execution Time (microsec)")
plt.title("Time Complexity Graph")
plt.legend()
plt.show()