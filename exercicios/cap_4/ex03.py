matrix = [[1,2],[3,4],[5,6],[7,8]]

matrix_t=list(map(lambda *i: [j for j in i], *matrix))

print(matrix_t)