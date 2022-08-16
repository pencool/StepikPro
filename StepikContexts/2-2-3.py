original, changed = input(), input()
for i in range(len(changed)-1):
    test = list(changed).copy()
    del test[i]
    if original == ''.join(test):
         print(changed[i])