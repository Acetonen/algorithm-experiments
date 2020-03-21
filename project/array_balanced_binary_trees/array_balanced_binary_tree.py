def recursively_fill_tree(index, array, result_tree):
    if not array:
        return

    sub_index = len(array) // 2
    result_tree[index] = array[sub_index]

    left_side = array[:sub_index]
    right_side = array[sub_index + 1:]
    left_child = 2 * index + 1
    right_child = 2 * index + 2

    recursively_fill_tree(left_child, left_side, result_tree)
    recursively_fill_tree(right_child, right_side, result_tree)


def GenerateBBSTArray(array):
    array = sorted(array)
    result_tree = [None for _ in array]

    recursively_fill_tree(0, array, result_tree)
    return result_tree
