def minimum(arr, index):
    new_index = index
    for i in range(index + 1, len(arr)):
        if arr[i] < arr[index]:
            new_index = i
    return new_index


def selection_sort(arr):
    for i in range(0, len(arr)):
        current_index = i
        new_index = minimum(arr, current_index)
        if new_index != current_index:
           arr[current_index], arr[new_index] = arr[new_index], arr[current_index]
    return 0