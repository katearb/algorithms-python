import random

def binary_search(number: int, list_: list, high=None, low=0):
    if high is None:
        high = len(list_) - 1
    elif low > high:
        return False

    mid = (high + low) // 2
    if list_[mid] == number:
        print('было загадано: ', list_100[mid])
        return 'индекс загаданного числа ' + str(mid)
    else:
        if number > list_[mid]:
            return binary_search(number, list_, high, mid+1)
        else:
            return binary_search(number, list_, mid-1, low)


list_100 = [i for i in range(1, 101) if i % 2 == 0]
random_n = random.choice(list_100)

print(binary_search(random_n, list_100))
