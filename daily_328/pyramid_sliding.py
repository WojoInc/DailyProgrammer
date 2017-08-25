num_rows = int(input())
i = 0
pyramid = []
while i < num_rows:
    row = input()
    nodes = row.split(" ")
    for node in nodes:
        if (i > 0):
            pyramid.append(int(node) + pyramid[int((len(pyramid) - 1) / 2)])
        else:
            pyramid.append(int(node))
    i += 1
short = -1
while i > 0:
    if short == -1 or pyramid[len(pyramid) - 1 - i] < short:
        short = pyramid[len(pyramid) - 1 - i]
    i -= 1
for node in pyramid:
    print(node)
print("Length of shortest path is: ", short)
