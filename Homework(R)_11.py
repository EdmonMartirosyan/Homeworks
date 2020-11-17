# 1

# def rotateImage(matrix):
#     rotated_list = []
#     rotated_matrix = []
#     j = 0
#     for _ in range(len(matrix)):
#         for i in range(len(matrix) - 1, -1, -1):
#             rotated_list.append(matrix[i][j])
#         rotated_matrix.append(rotated_list)
#         rotated_list = []
#         j += 1
#     return rotated_matrix
#
# exsample_1 = [[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]]
# exsample_2 = [[10, 9, 6, 3, 7],
#               [6, 10, 2, 9, 7],
#               [7, 6, 3, 8, 2],
#               [8, 9, 7, 9, 9],
#               [6, 8, 6, 8, 2]]
#
# print(rotateImage(exsample_2))


# 2

def digitsProduct(product):
    n = 2
    factors = []
    if product == 1:
        return 1
    while product//n > 0:
        if product % n == 0:
            factors.append(n)
            product = product//n
        else:
            n += 1
    if len(factors) == 1:
        return -1
    if len(factors) != 0:
        new_factors = []
        factors_string = ""
        new_factors.append(factors[0])
        i = 1
        j = 2
        while j < len(factors):
            if factors[i]*factors[j] < 10:
                new_factors.append(factors[i]*factors[j])
            else:
                new_factors.append(factors[i])
                new_factors.append(factors[j])
            i += 2
            j += 2
        new_factors.sort()
        for elem in new_factors:
            factors_string += str(elem)
        return int(factors_string)
    else:
        return 10


print(digitsProduct())










