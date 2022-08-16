import re

resnames = [re.sub(r'\d*@.+', '', input()) for i in range(int(input()))]
for i in range(int(input())):
    x = input()
    if x in resnames:
        print(f'{x}{resnames.count(x)}@beegeek.bzz')
        resnames.append(x)
    else:
        print(f'{x}@beegeek.bzz')
        resnames.append(x)