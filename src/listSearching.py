def binary_search(list_name, left, right, goal):
    if right >= left:
        mid = left + (right - left) // 2

        if list_name[mid] == goal:
            return mid

        elif list_name[mid] < goal:
            return binary_search(list_name, mid + 1, right, goal)

        else:
            return binary_search(list_name, left, mid - 1, goal)

    else:
        return -1
