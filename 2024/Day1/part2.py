with open('2024/Day1/input.txt', 'r') as input:
    list1 = []
    list2 = []
    for line in input:
        num1 = str(line[0]) + str(line[1]) + str(line[2]) + str(line[3]) + str(line[4])
        num2 = str(line[8]) + str(line[9]) + str(line[10]) + str(line[11]) + str(line[12])
        list1.append(num1)
        list2.append(num2)
    scoreTotal = 0
    for leftNum in list1:
        multiplier = 0
        for rightNum in list2:
            if rightNum == leftNum:
                multiplier += 1
                print(f'{rightNum} equals {leftNum}, multiplier is now {multiplier}')
        print(f'{leftNum} was found {multiplier} times in Right list.')
        scoreIncrease = int(leftNum) * multiplier
        scoreTotal += scoreIncrease
    print(scoreTotal)