def choice_sort(array: list):
    """
    sorts the given list
    :param array: list of numbers
    :return: sorted list
    """
    sorted_array = list(array)
    N = len(sorted_array)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if sorted_array[pos] > sorted_array[k]:
                sorted_array[pos], sorted_array[k] = sorted_array[k], sorted_array[pos]

    return sorted_array


if __name__ == '__main__':
    array = [-1, 44, 5, 33, 4, 53, 5, 0]
    print(choice_sort(array))