x = [101, 57, 6, 98, 32, 0, 57, 98]

for i in range(len(x)):
    for j in range(i + 1, len(x)):
        if x[i] == x[j]:
            print(x[i])