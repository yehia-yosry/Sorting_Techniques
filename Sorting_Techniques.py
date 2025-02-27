import time
import random

def bubble_sort(arr):
    for i in range(0, len(arr)):
        is_sorted = True
        for j in range(0, len(arr) - 1 - i):
            if(arr[j] > arr[j+1]):
                is_sorted = False
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if is_sorted == True:
            break
    return arr

def insertion_sort(arr):
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
    return arr

def selection_sort(arr):
    for i in range(0, len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Random Array Generating Function
def rand_arr(length):
    arr = []
    for i in range(0, int(length)):
        arr.insert(0, random.randint(0, 12000))
    print("Random Array Generated: ", "\n",  arr)
    return arr
        
  
arr_length = input("Enter Array Length To Test Sorting Algorithms On: ")
arr = rand_arr(arr_length)

# Testing Bubble Sort
begin1 = time.time()
print(bubble_sort(arr))
end1 = time.time()
        
# Testing Insertion Sort
begin2 = time.time()
print(insertion_sort(arr))
end2 = time.time()

# Testing Selection Sort
begin3 = time.time()
print(selection_sort(arr))
end3 = time.time()


print("Bubble Sort: " ,  end1 - begin1)
print("Insertion Sort: " ,  end2 - begin2)
print("Selection Sort: " ,  end3 - begin3)