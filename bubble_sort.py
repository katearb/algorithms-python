def bubble_sort(number_list: list):
    """
    Sort the given list
    :param number_list: a list of any numbers
    :return: None
    """
    for i in range(len(number_list)):
        for index, item in enumerate(number_list):
            if index == len(number_list) - 1:
                break

            elif item > number_list[index + 1]:
                number_list[index] = number_list[index + 1]
                number_list[index + 1] = item


if __name__ == "__main__":
    number_list = [16, -15, -19, 10, 17]
    bubble_sort(number_list)
    print(number_list)
