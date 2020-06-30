import random


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = random.choice(array)
        del array[array.index(pivot)]
        less = [i for i in array if i < pivot]
        greater = [i for i in array if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([2, 4, 66, 34, 43, 100]))

