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
    rounded.append(round(coordinates[count][0]/Dx))
    rounded.append(round(coordinates[count][1]/Dy)-1)
    count = count+1

print(rounded)
for i in range(0, len(rounded)-1, 2):
    print(str(rounded[i]) + " " + str(rounded[i+1]))

"""
8 8 0.5 0.5 3
2.439498 1.2343
0.2348973 4.587536
0.75 1.25
"""