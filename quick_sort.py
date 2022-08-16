import random


def quick_sort(array: list):  # O(n^2), av: O(nlog(n))
    """
    sorts a list
    :param array: list of numbers
    :return: sorted list
    """
    if len(array) < 2:
        return array

    pivot = random.choice(array)
    del array[array.index(pivot)]
    less = [i for i in array if i < pivot]
    greater = [i for i in array if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    print(quick_sort([0, -1000, -1, 2, 4, 66, 34, 43, 100]))

