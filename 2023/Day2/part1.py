with open('2023\Day2\input.txt', 'r') as input:
    list = list(enumerate(input, 1))
    total_len = len(list)
    print(total_len)
    possible_games = []
    for i in range(total_len):
        id = list[i][0]
        line_string = str(list[i])
        red_list = line_string.split("red")
        list_len = len(red_list) - 1
        count = 0
        print(line_string)
        print(red_list)
        print(f"Parsing game {id}.. with {list_len} red instances.")
        for i in range(list_len):
            item = red_list[i]
            r = ""
            r += item[-3]
            r += item[-2]
            red_num = int(r)
            print(red_num)
            if red_num <=12:
                count += 1
                continue
            if red_num > 12:
                print(f"{id} was impossible")
                break
        if count == list_len:
            print(f"{id} was possible, adding to list.")
            possible_games.append(id)

    possible_games_2 = []
    for each_id in possible_games:
        id = each_id
        index = int(each_id) - 1
        line_string = str(list[index])
        blue_list = line_string.split("blue")
        list_len = len(blue_list) - 1
        count = 0
        for i in range(list_len):
            item = blue_list[i]
            b = ""
            b += item[-3]
            b += item[-2]
            blue_num = int(b)
            if blue_num <= 14:
                count += 1
                continue
            if blue_num > 14:
                print(f'{id} was impossible')
                break
        if count == list_len:
            print(f"{id} possible, adding to new list.")
            possible_games_2.append(id)
    possible_games_3 = []
    for each_id in possible_games_2:
        id = each_id
        index = int(each_id) - 1
        line_string = str(list[index])
        green_list = line_string.split("green")
        list_len = len(green_list) - 1
        count = 0
        for i in range(list_len):
            item = green_list[i]
            g = ""
            g += item[-3]
            g += item[-2]
            green_num = int(g)
            if green_num <= 13:
                count += 1
                continue
            if green_num > 13:
                print(f'{id} was impossible')
                break
        if count == list_len:
            print(f"{id} possible, adding to new list.")
            possible_games_3.append(id)
    sum = 0
    for each_id in possible_games_3:
        sum += each_id
    print(sum)