# 1

def func(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in range(len(str2)):
        if str2.count(str2[i]) != str1.count(str2[i]):
            return False
    return True


print(func("abvdj", "vjdab"))


# 2

# matrix = [[10, 20, 30, 40],
#            [15, 25, 35, 45],
#            [27, 29, 37, 48],
#            [32, 33, 39, 50]]

# def search(matrix, number):
#     for i in range(len(matrix)):
#         left = 0
#         right = len(matrix[i])-1
#         while left <= right:
#             middle = (left + right)//2
#             if number < matrix[i][middle]:
#                 right = middle-1
#             elif number > matrix[i][middle]:
#                 left = middle+1
#             else:
#                 return i, middle
#
#
# print(search(matrix, 29))
