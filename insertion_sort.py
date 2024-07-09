def insertion_sort(arr):
    for current_index in range(0, len(arr)-1):
        print(current_index)
        comparison_index = current_index + 1

        while current_index >= 0 and arr[current_index] > arr[comparison_index]:
            arr[comparison_index], arr[current_index] = arr[current_index], arr[comparison_index]
            comparison_index -= 1
            current_index -= 1
            print(arr)
    return 0
