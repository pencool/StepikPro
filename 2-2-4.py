numbers = input().split()
numcntd = {}
for i in numbers:
    numcntd[i] = numbers.count(i)
for k, v in sorted(numcntd.items()):
    if v > 1:
        print(k, end=' ')