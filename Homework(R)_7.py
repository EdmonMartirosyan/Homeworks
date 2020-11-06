#1
# def answer_queries(k, *query_counts):
#     balance = 0
#     day = 0
#     for elem in query_counts:
#         day += 1
#         b = balance
#         if elem > k:
#             balance += elem-k
#         elif elem < k:
#             if balance > 0:
#                 balance -= k-elem
#         if balance <= 0 and b+elem != k:
#             return day
#     while balance >= 0:
#         balance -= k
#         day += 1
#     return day
#
#
# print(answer_queries(1, 100))

#2
def non_decreasing_sequence(*nums):
    list_1 = list(nums)
    for i in range(1,len(list_1)-1):
        if list_1[i] < list_1[i-1]:
            list_1[i-1] = -list_1[i-1]
            if list_1[i-1] == 0:
                for _ in range(len(list_1)):
                    i -= 1
                    list_1[i-1] = -list_1[i-1]
        if list_1[i] > list_1[i+1]:
            list_1[i+1] = -list_1[i+1]
            if list_1[i+1] == 0:
                for _ in range(len(list_1)):
                    i -= 1
                    list_1[i+1] = -list_1[i+1]
    if list_1 == sorted(list_1):
        print("Yes", list_1, sep="\n")
    else:
        print("No")


non_decreasing_sequence()
