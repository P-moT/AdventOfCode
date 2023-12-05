with open('2023\Day3\input.txt', 'r') as input:
    lines = []
    final_numbers = []
    for line in input:
        lines.append(line.strip('\n'))
    for i in range(140):
        next_line = []
        prev_line = []
        current_line = lines[i]
        if i != 0:
            prev_line = lines[i-1]
        if i != 139:
            next_line = lines[i+1]
        current_num = ''
        added_num = ''
        print(f"Parsing line {i+1}")
        for char_index in range(140):
            char = current_line[char_index]
            if char == '.':
                current_num = ''
                added_num = ''
                continue
            if char.isdigit() and current_num == '':
                current_num += char
                if char_index < 139 and current_line[char_index+1].isdigit():
                    current_num += current_line[char_index+1]
                    if char_index <138 and current_line[char_index+2].isdigit():
                        current_num += current_line[char_index+2]
            if char.isdigit():
                if char_index != 0 and char_index != 139:
                    if not current_line[char_index-1].isdigit() and current_line[char_index-1] != '.':
                        print(f'{current_num} is a part number!')
                        added_num = current_num
                        final_numbers.append(current_num)
                        current_num = ''
                        continue
                    if not current_line[char_index+1].isdigit() and current_line[char_index+1] != '.':
                        print(f'{current_num} is a part number!')
                        added_num = current_num
                        final_numbers.append(current_num)
                        current_num = ''
                        continue
                    if len(prev_line) > 1 and len(next_line) > 1:
                        if (prev_line[char_index] != '.'
                            or prev_line[char_index -1] != '.'
                            or prev_line[char_index + 1] != '.'
                            or next_line[char_index] != '.'
                            or next_line[char_index - 1] != '.'
                            or next_line[char_index + 1] != '.'):
                            if added_num == '':
                                print(f'{current_num} is a part number!')
                                added_num = current_num
                                final_numbers.append(current_num)
                                current_num = ''
                    elif len(prev_line) > 1:
                        if (prev_line[char_index] != '.'
                            or prev_line[char_index -1] != '.'
                            or prev_line[char_index + 1] != '.'):
                            if added_num == '':
                                print(f'{current_num} is a part number.')
                                added_num = current_num
                                final_numbers.append(current_num)
                                current_num = ''
                    elif len(next_line) > 1:
                        if (next_line[char_index] != '.'
                            or next_line[char_index -1] != '.'
                            or next_line[char_index + 1] != '.'):
                            if added_num == '':
                                print(f'{current_num} is a part number...')
                                added_num = current_num
                                final_numbers.append(current_num)
                                current_num = ''
                    continue
                if char_index == 0:
                    if not current_line[char_index+1].isdigit() and current_line[char_index+1] != '.':
                        print(f'{current_num} is a part number!')
                        added_num = current_num
                        final_numbers.append(current_num)
                        current_num = ''
                        continue
                    if len(prev_line) > 1 and len(next_line) > 1:
                        if (prev_line[char_index] != '.'
                            or prev_line[char_index + 1] != '.'
                            or next_line[char_index] != '.'
                            or next_line[char_index + 1] != '.'):
                            if added_num == '':
                                print(f'{current_num} is a part number!')
                                final_numbers.append(current_num)
                                added_num = current_num
                                current_num = ''
                    elif len(prev_line) > 1:
                        if (prev_line[char_index] != '.'
                            or prev_line[char_index + 1] != '.'):
                            if added_num == '':
                                print(f'{current_num} is a part number.')
                                final_numbers.append(current_num)
                                added_num = current_num
                                current_num = ''
                    elif len(next_line) > 1:
                        if (next_line[char_index] != '.'
                            or next_line[char_index + 1] != '.'):
                            if added_num == '':
                                print(f'{current_num} is a part number...')
                                final_numbers.append(current_num)
                                added_num = current_num
                                current_num = ''
                    continue
                if char_index == 139:
                    if not current_line[char_index-1].isdigit() and current_line[char_index-1] != '.':
                        print(f'{current_num} is a part number!')
                        added_num = current_num
                        final_numbers.append(current_num)
                        current_num = ''
                        continue
                    if len(prev_line) > 1 and len(next_line) > 1:
                        if (prev_line[char_index] != '.'
                            or prev_line[char_index -1] != '.'
                            or next_line[char_index] != '.'
                            or next_line[char_index - 1] != '.'):
                            if added_num == '':
                                print(f'{current_num} is a part number!')
                                final_numbers.append(current_num)
                                added_num = current_num
                                current_num = ''
                    elif len(prev_line) > 1:
                        if (prev_line[char_index] != '.'
                            or prev_line[char_index -1] != '.'):
                            if added_num == '':
                                print(f'{current_num} is a part number.')
                                final_numbers.append(current_num)
                                added_num = current_num
                                current_num = ''
                    elif len(next_line) > 1:
                        if (next_line[char_index] != '.'
                            or next_line[char_index -1] != '.'):
                            if added_num == '':
                                print(f'{current_num} is a part number...')
                                final_numbers.append(current_num)
                                added_num = current_num
                                current_num = ''
                    continue
    sum = 0
    for each_number in final_numbers:
        sum += int(each_number)
    print(sum)


