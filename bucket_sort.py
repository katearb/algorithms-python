from functools import reduce
from math import ceil


def bucket_sort(number_list: list):  # O(n^2)
    """
    :param number_list: a list of non-negative numbers
    :return: sorted list
    """
    buckets_num = round(len(number_list) / 2)
    buckets = [[] for _ in range(buckets_num)]
    step = (max(number_list) - min(number_list)) // buckets_num + 1  # range of each bucket
    for index, bucket in enumerate(buckets):
        for item in number_list:
            start = index * step
            end = index * step + step
            if start <= item <= end:
                buckets[index].append(item)

    buckets = list(map(sorted, buckets))
    return list(reduce(list.__add__, buckets))


if __name__ == "__main__":
    number_list = [10, 12, 3, 1, 4, 5, 22, 34, 36, 45, 46, 77, 0]
    print(bucket_sort(number_list))
