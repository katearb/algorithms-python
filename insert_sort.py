def insert_sort(array: list):
    """
    sort the given list
    :param array: list of any numbers
    :return: None
    """
    N = len(array)
    for index in range(1, N):  # go from 1 to N
        for i in range(index, 0, -1):  # go from index to 0
            if array[i] < array[i - 1]:  # if (greater, smaller)
                array[i], array[i-1] = array[i-1], array[i]  # (greater, smaller)->(smaller, greater)
            else:
                break


if __name__ == '__main__':
    array = [3, 4, 2,-1, 3, 3]
    insert_sort(array)
    print(array)