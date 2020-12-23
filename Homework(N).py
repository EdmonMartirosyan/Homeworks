# 1

# def func(n):
#     a = 1
#     b = 10
#     i = 2
#     while i <= n:
#         if i >= b:
#             b *= 10
#         a *= b
#         a += i
#         i += 1
#     return a


# print(func(18))

# 2

# i = 0
# j = 3
# def find_counterfeit_coin(coins):
#     global i
#     global j
#     if sum(coins[i:j]) % 2 == 1:
#         print(coins.index(1))
#     else:
#         i += 1
#         j += 3
#         find_counterfeit_coin(coins)
#
#
# find_counterfeit_coin([2, 2, 2, 2, 2, 2, 2, 1])


# 3
# def sort_list_elements(numbers):
#     sorted_list = []
#     for i in range(0, len(numbers)):
#         if numbers[i] != -1:
#             sorted_list.append(numbers[i])
#     sorted_list.sort()
#     for i in range(0, len(numbers)):
#         if numbers[i] == -1:
#             sorted_list.insert(i, numbers[i])
#     return sorted_list


#print(sort_list_elements([2, -1, 1, 5, 4, -1, 3]))
