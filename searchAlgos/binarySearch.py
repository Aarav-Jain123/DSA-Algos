def binary_search(array, item, low_index=0, high_index=None):
    if high_index is None:
        array.sort()  # ensure sorted once
        high_index = len(array) - 1

    if low_index <= high_index:
        middle_index = (low_index + high_index) // 2

        if array[middle_index] == item:
            return middle_index  # return index
        elif array[middle_index] < item:
            return binary_search(array, item, middle_index + 1, high_index)
        else:
            return binary_search(array, item, low_index, middle_index - 1)
    else:
        return -1  # not found


# Example
print(binary_search([2, 3, 5, 4, 5, 1, 5], 5))  # Output: 1 (after sorting -> [1,2,3,4,5,5,5])

# print(binary_search([2, 3, 5, 4, 5, 1, 5], 2))


