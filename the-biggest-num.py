def biggest_n(list_):
    if len(list_) > 1:
        if list_[0] >= list_[1]:
            del list_[1]
            return biggest_n(list_)
        else:
            del list_[0]
            return biggest_n(list_)
    else:
        return list_[0]


print(biggest_n([1, 2, 6, 3]))
print(biggest_n([111, 11, 1]))
