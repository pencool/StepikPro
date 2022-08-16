numbers = [*map(int, input().split())]
lstnumbers = [i for i in range(1, numbers[0]+1)]
lstnumbers[numbers[1]-1:numbers[2]] = lstnumbers[numbers[1]-1:numbers[2]][::-1]
lstnumbers[numbers[3]-1:numbers[4]] = lstnumbers[numbers[3]-1:numbers[4]][::-1]
print(*lstnumbers)