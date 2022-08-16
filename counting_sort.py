def counting_sort(array: list):
    """
    sots the given array
    :param array: list of non-negative numbers
    :return: sorted list
    """
    max_element = max(array)

    count_array = [0] * (max_element +1)

    for elem in array:
        count_array[elem] += 1

    sorted_array = []
    for i, count in enumerate(count_array):
        sorted_array.extend([i]*count)

    return sorted_array


if __name__ == '__main__':
    array = [0, 12, 32, 54, 45, 765, 9, 45]
    print(counting_sort(array))