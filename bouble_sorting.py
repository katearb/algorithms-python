number_list = [16, -15, -19, 10, 17]


for i in range(len(number_list)):
    for index, item in enumerate(number_list):
        if index == len(number_list) - 1:
            continue

        elif item < number_list[index + 1]:
            number_list[index] = number_list[index + 1]
            number_list[index + 1] = item

print(number_list)
