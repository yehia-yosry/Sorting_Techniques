import time

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
    

# Testing Bubble Sort
begin = time.time()
print(bubble_sort([5, 4, 3, 2, 1]))
end = time.time()
print("Bubble Sort: " ,  end - begin)
        
# Testing Insertion Sort
begin = time.time()
print(insertion_sort([5, 4, 3, 2, 1]))
end = time.time()
print("Insertion Sort: " ,  end - begin)


# Testing Selection Sort
begin = time.time()
print(selection_sort([5, 4, 3, 2, 1]))
end = time.time()
print("Selection Sort: " ,  end - begin)