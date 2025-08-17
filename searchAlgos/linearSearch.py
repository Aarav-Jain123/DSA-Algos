def linear_search(array, item):
    for index in range(len(array)):
        if array[index] == item:
            return index
    return -1


print(linear_search([1, 2, 3, 5, 4, 5, 2, 1, 5], 4))  # Output: 4
