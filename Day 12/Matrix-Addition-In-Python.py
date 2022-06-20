X = [[34,76,3],
    [19 ,67,12],
    [9 ,23,90]]

Y = [[52,81,21],
    [23,14,33],
    [92,28,29]]

res= [[0,0,0],
    [0,0,0],
    [0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       res[i][j] = X[i][j] + Y[i][j]

for r in res:
   print(r)