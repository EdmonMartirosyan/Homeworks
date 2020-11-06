#1

# def books_authors(author_name, **book_details):
#     books_list = list(book_details.items())
#     books_dict = {}
#     for i in range(len(books_list)):
#         if books_list[i][1][0] == author_name:
#             books_dict[books_list[i][1][1]] = books_list[i][0]
#     for i in sorted(books_dict.keys()):
#         print(books_dict[i])
#
#
# books_authors("Tolstoy", Resurrection=["Tolstoy", 1899], WarAndPeace=["Tolstoy", 1869], TheShot=["Pushkin", 1830], TheCossacks=["Tolstoy", 1863])



#2

# def largest_composition(integers_list):
#     integers_list.sort()
#     return integers_list[-3]*integers_list[-2]*integers_list[-1]
#
#
# print(largest_composition([9,5,8,5,20,1,2,-3,-2,-1,0]))
