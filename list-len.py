def n_items(list_):
    if len(list_) == 0:
        return 0
    else:
        return 1 + len(list_[1:])


print(n_items([1, 2, 3, 4]))
