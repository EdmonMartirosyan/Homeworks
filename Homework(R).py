def swap_list_elements(listt):
    swaped_list = []
    pair_index = 0
    odd_index = 1
    for i in range(0,len(listt)):
        if listt[i] % 2 == 0:
            swaped_list.insert(pair_index, listt[i])
            pair_index += 2
        else:
            swaped_list.insert(odd_index, listt[i])
            odd_index += 2
    return swaped_list


print(swap_list_elements([1, 4, 6, 5, 7, 10]))