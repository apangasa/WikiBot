def binary_search(list_name, left, right, to_find):
    if right >= left:
        mid = left + (right - left) // 2

        if list_name[mid] == to_find:
            print(to_find)
            return mid

        elif list_name[mid] < to_find:
            return binary_search(list_name, mid + 1, right, to_find)

        else:
            return binary_search(list_name, left, mid - 1, to_find)

    else:

        return -1
