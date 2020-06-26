def sum(number_list: list):
    if len(number_list) == 0:
        return 0
    else:
        return number_list[0] + sum(number_list[1:])


print(sum([2, 4, 6]))
