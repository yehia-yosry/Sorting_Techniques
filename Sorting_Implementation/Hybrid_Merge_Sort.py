import Insertion_Sort as IS


def merge_sort(arr, THRESHOLD):
    copy = arr[:]
    if len(copy) <= THRESHOLD:
        return IS.Insertion_Sort(copy)[0]
    mid = len(copy) // 2
    left_arr = copy[0:mid]
    right_arr = copy[mid: len(copy)]
    return merge(merge_sort(left_arr, THRESHOLD), merge_sort(right_arr, THRESHOLD))


def merge(left_arr, right_arr):
    sorted_array = []
    while len(left_arr) > 0 and len(right_arr) > 0:
        if left_arr[0] <= right_arr[0]:
            sorted_array.append(left_arr.pop(0))
        else:
            sorted_array.append(right_arr.pop(0))
    sorted_array.extend(left_arr)
    sorted_array.extend(right_arr)
    return sorted_array


print(merge_sort([8, 6, 4, 8, 3, 6, 1], 5))
