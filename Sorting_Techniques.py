
import random
import matplotlib.pyplot as plt  # type: ignore
import bubble_sort as bs  # type: ignore
import insertion_sort as ins  # type: ignore
import selection_sort as ss  # type: ignore


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
        time_bubble.append(bs.bubble_sort(arr)[1])
        time_insertion.append(ins.insertion_sort(arr)[1])
        time_selection.append(ss.selection_sort(arr)[1])
    return time_bubble, time_insertion, time_selection


input_sizes = [0, 2500, 5000, 7500, 10000]
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
