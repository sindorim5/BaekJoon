import copy

matrix = [[1,2,3,4,5], [5,4,3,2,1]]
cleanM = copy.deepcopy(matrix)
matrix[0][0] = 9
for m in matrix:
  print(m)


print("************************")
matrix = cleanM[:]
for m in matrix:
  print(m)