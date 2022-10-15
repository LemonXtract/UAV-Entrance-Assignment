import math

N, M, Dx, Dy, k = list(map(float, input("Enter coordinates: ").split()))
k = int(k)
N = int(N)
M = int(M)

coordinates = []
rounded = []

for i in range(k):
    coordinates.append(list(map(float, input("Enter coordinates: ").split())))
    print(coordinates)

count = 0

while count != k:
    for i in range(N):
        if math.isclose(coordinates[count][0], Dx*i, rel_tol = 0.24):
            rounded.append(Dx*i)
    count = count+1

count = 0

while count != k:
    for i in range(M):
        if math.isclose(coordinates[count][1], Dy*i, rel_tol = 0.24):
            rounded.append(round(Dy*i))
    count = count+1

print(rounded)

"""
8 8 0.5 0.5 3
2.439498 1.2343
0.2348973 4.587536
0.75 1.25
"""