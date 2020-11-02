def sort_list_elements(numbers):
    sorted_list = []
    for i in range(0, len(numbers)):
        if numbers[i] != -1:
            sorted_list.append(numbers[i])
    sorted_list.sort()
    for i in range(0, len(numbers)):
        if numbers[i] == -1:
            sorted_list.insert(i, numbers[i])
    return sorted_list


print(sort_list_elements([2, -1, 1, 5, 4, -1, 3]))
