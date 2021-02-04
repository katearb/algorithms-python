from functools import reduce

number_list = [10, 12, 3, 1, 4, 5, 22, 34, 36, 45]
buckets_num = round(len(number_list) / 2)
buckets = [[] for i in range(buckets_num)]
step = (max(number_list) - min(number_list)) / buckets_num

for index, bucket in enumerate(buckets):
    for item in number_list:
        start = (index * step)
        end = (index * step + step)
        if (index * step) + 1 <= item < (index * step + step) + 1:
            buckets[index].append(item)

buckets = list(map(sorted, buckets))
sorted_list = list(reduce(list.__add__, buckets))
print(sorted_list)
