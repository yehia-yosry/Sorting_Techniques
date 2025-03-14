def merge_sort(arr):
    copy = arr[:]
    if len(copy) < 2:
        return copy
    mid = len(copy) // 2
    left_arr = copy[0:mid]
    right_arr = copy[mid: len(copy)]
    return merge(merge_sort(left_arr), merge_sort(right_arr))


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
