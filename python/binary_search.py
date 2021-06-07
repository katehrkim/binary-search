def binary_search(number_to_find, sorted_values):
    sorted_values.sort()
    lower = 0
    upper = len(sorted_values)
    diff = upper - lower
    while diff >= 1:
        middle = diff // 2 + lower
        if sorted_values[middle] == number_to_find:
            return middle
        elif sorted_values[middle] < number_to_find:
            lower = middle + 1
            diff = upper - lower
        elif sorted_values[middle] > number_to_find:
            upper = middle
            diff = upper - lower
    return -1


