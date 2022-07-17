from copy import deepcopy


def n_arr(sizes):
    size = len(sizes)

    if size == 0:
        return []

    last_size = sizes[-1]
    sizes.remove(sizes[-1])
    if size < 2:
        return ['“”'] * last_size
    else:
        nested_arr = n_arr(sizes)
        return [deepcopy(nested_arr) for i in range(last_size)]


print(n_arr([2, 2, 2]))