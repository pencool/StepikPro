def beegeek(a, b):
    answer = []
    for i in range(a, b+1):
        if i % 3 == 0 and i % 7 == 0:
            answer.append('BeeGeek')
        elif i % 3 == 0:
            answer.append('Bee')
        elif i % 7 ==0:
            answer.append('Geek')
        else:
            answer.append(str(i))
    return ' '.join(answer)

print(beegeek(14, 21))