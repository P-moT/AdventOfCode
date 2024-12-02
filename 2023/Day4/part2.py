from collections import defaultdict
with open('2023\Day4\input.txt', 'r') as input:
    lines = []
    cards = defaultdict(int)
    for line in input:
        lines.append(line.strip('\n'))
    for each_line in lines:
        count = 0
        line_string = str(each_line)
        numbers = line_string.split(':')
        card_string = numbers[0].split(' ')
        card_id = (int(card_string[-1]))
        sn = numbers[1].split('|')
        winning_num_string = sn[0].split(' ')
        winning_nums = []
        cards[card_id] += 1
        for each_string in winning_num_string:
            if each_string.isdigit():
                winning_nums.append(each_string)
        my_num_string = sn[1].split(' ')
        my_nums = []
        for each_string in my_num_string:
            if each_string.isdigit():
                my_nums.append(each_string)
        for each_num in my_nums:
            for each_winning_num in winning_nums:
                if each_num == each_winning_num:
                    count += 1
        print(card_id, count)
        for i in range(count):
            cards[card_id+1+i] += cards[card_id]
    sum = 0
    print(cards)
    for each_card in cards:
        sum += cards[each_card]
    print(sum)



