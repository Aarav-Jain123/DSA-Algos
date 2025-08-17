# No duplicates
def binary_search(array, item):
    low_index = 0
    high_index = len(array) - 1
    array.sort()
    while low_index <= high_index:
        middle_index = high_index // 2
        if array[middle_index] == item:
            return item
        elif array[middle_index] < item:
            array = array[middle_index:]
            binary_search(array, item)
        elif array[middle_index] > item:
            array = array[:middle_index]
            print(array)
            binary_search(array, item)
        else:
            return -1


print(binary_search([2, 3, 5, 4, 5, 1, 5], 2))
