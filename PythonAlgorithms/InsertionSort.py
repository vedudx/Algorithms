listi = list(map(int, input().split()))

for i in range(1, len(listi)):

    temp = listi[i]
    pos = i
    while pos - 1 >= 0 and listi[pos - 1] > temp:
        listi[pos] = listi[pos-1]
        pos -= 1
    listi[pos] = temp

print(listi)