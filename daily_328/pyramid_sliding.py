num_rows = int(input())
i = 0
pyramid = []
while i < num_rows:
    row = input()
    nodes = row.split(" ")
    pyramid.append([])
    for node in nodes:
        pyramid[i].append(int(node))

    i += 1

for i in range(0, num_rows - 1):
    for j in range(0, len(pyramid[i])):
        pyramid[i + 1][j] += pyramid[i][j]
        pyramid[i + 1][j + 1] += pyramid[i][j]

short = -1
for res in pyramid[-1]:
    if short == -1 or res < short:
        short = res
for node in pyramid:
    print(node)
print("Length of shortest path is: ", short)
