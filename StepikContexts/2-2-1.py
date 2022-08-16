ln = int(input())
answer = []
count = 0
end = True
while end:
    for i in range(1, ln+1):
        for j in range(i):
            answer.append(i)
        if len(answer) >= ln:
            end = False
            break
    count += 1
print(*answer[:ln])