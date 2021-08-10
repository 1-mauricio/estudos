m = []
for i in range(3):
    m.append([0]*4)

for i in range (3):
    for j in range(4):
        m[i][j] = 10*(i+j) + j + 1

for i in range (3):
    print (m[i])