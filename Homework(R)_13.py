# 1

# def financialCrisis(roadRegister):
#     finalyRoadRegisters = []
#     changedRoadRegister = []
#     k = 0
#     while k < len(roadRegister):
#         for i in range(len(roadRegister)):
#              new_roads = [roadRegister[i][j] for j in range(len(roadRegister[i])) if i != k and j != k]
#              if len(new_roads) != 0:
#               changedRoadRegister.append(new_roads)
#         finalyRoadRegisters.append(changedRoadRegister)
#         changedRoadRegister = []
#         k += 1
#     return finalyRoadRegisters
#
#
# ex1 = [[False, True, True, False],
#        [True, False, True, False],
#        [True, True, False, True],
#        [False, False, True, False]]
#
# print(financialCrisis(ex1))


# 2

# def namingRoads(roads):
#     roads_dict = {roads[i][2]: set(roads[i][0:2]) for i in range(len(roads))}
#     for i in range(len(roads)-1):
#         if roads_dict[i] & roads_dict[i+1]:
#             return False
#     return True
#
#
# ex1 = [[0, 1, 0],
#        [4, 1, 2],
#        [4, 3, 4],
#        [2, 3, 1],
#        [2, 0, 3]]
#
# print(namingRoads(ex1))