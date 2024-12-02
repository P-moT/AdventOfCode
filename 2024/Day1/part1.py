with open('2024/Day1/input.txt', 'r') as input:
    list1 = []
    list2 = []
    for line in input:
        num1 = str(line[0]) + str(line[1]) + str(line[2]) + str(line[3]) + str(line[4])
        num2 = str(line[8]) + str(line[9]) + str(line[10]) + str(line[11]) + str(line[12])
        list1.append(num1)
        list2.append(num2)
    list.sort(list1)
    list.sort(list2)
    i = 0
    totalDistance = 0
    while i < 1000:
        distance = abs(int(list1[i]) - int(list2[i]))
        totalDistance += distance
        i += 1
