# 1

# def newRoadSystem(roadRegister):
#     cities_with_access = []
#     cities_with_exit = []
#     for i in range(len(roadRegister)):
#         for j in range(len(roadRegister[i])):
#             if roadRegister[i][j] == True:
#                 cities_with_access.append(i)
#                 cities_with_exit.append(j)
#     if sorted(cities_with_access) == sorted(cities_with_exit):
#         return True
#     return False
#
#
# ex1 = [[False, True, False, False],
#        [False, False, True, False],
#         [True, False, False, True],
#        [False, False, True, False]]
#
# print(newRoadSystem(ex1))


# 2

# def efficientRoadNetwork(n, roads):
#     all_roads = {tuple(i) for i in roads}
#     for i in range(len(roads) - 1):
#         for j in range(i + 1, len(roads)):
#             if set(roads[i]) & set(roads[j]):
#                 all_roads.add(tuple(set(roads[i]) ^ set(roads[j])))
#     for i in range(n):
#         for j in range(i+1,n):
#             if (i,j) not in all_roads and (j,i) not in all_roads:
#                 return False
#     return True
#
#
# ex1 = [[3, 0],
#        [0, 4],
#        [5, 0],
#        [2, 1],
#        [1, 4],
#        [2, 3],
#        [5, 2]]
#
# print(efficientRoadNetwork(6, ex1))