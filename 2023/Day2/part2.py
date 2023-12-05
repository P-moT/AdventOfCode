high_reds = []
high_blues = []
high_greens =[]
high_products = []
with open('2023\Day2\input.txt', 'r') as input:
    list = list(enumerate(input, 1))
    total_len = len(list)
    possible_games = []
    for i in range(total_len):
        id = list[i][0]
        line_string = str(list[i])
        red_list = line_string.split("red")
        list_len = len(red_list) - 1
        count = 0
        high_red = 0
        for i in range(list_len):
            item = red_list[i]
            r = ""
            r += item[-3]
            r += item[-2]
            red_num = int(r)
            if red_num <= high_red:
                continue
            if red_num > high_red:
                high_red = red_num
            count += 1
        high_reds.append(high_red)

    for i in range(total_len):
        id = list[i][0]
        line_string = str(list[i])
        blue_list = line_string.split("blue")
        list_len = len(blue_list) - 1
        count = 0
        high_blue = 0
        for i in range(list_len):
            item = blue_list[i]
            b = ""
            b += item[-3]
            b += item[-2]
            blue_num = int(b)
            if blue_num <= high_blue:
                continue
            if blue_num > high_blue:
                high_blue = blue_num
        high_blues.append(high_blue)

    for i in range(total_len):
        id = list[i][0]
        line_string = str(list[i])
        green_list = line_string.split("green")
        list_len = len(green_list) - 1
        count = 0
        high_green = 0
        for i in range(list_len):
            item = green_list[i]
            g = ""
            g += item[-3]
            g += item[-2]
            green_num = int(g)
            if green_num <= high_green:
                continue
            if green_num > high_green:
                high_green = green_num
                continue
        high_greens.append(high_green)

    for i in range(len(high_reds)):
        high_products.append(high_reds[i] * high_blues[i] * high_greens[i])
    sum = 0
    for each_item in high_products:
        sum += each_item
    print(sum)