with open('2023\Day3\input.txt', 'r') as input:
    lines = []
    touching_numbers = []
    dict_of_gears = {}
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
            if not char.isdigit():
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
                    if current_line[char_index-1] == '*':
                        if added_num == '':
                            print(f'{current_num} is touching *!')
                            added_num = current_num
                            touching_numbers.append(current_num)
                            line_num = i+1
                            star_index = char_index -1
                            try:
                                if dict_of_gears[str(line_num)][str(star_index)]:
                                    dict_of_gears[str(line_num)][str(star_index)].append(current_num)
                            except:
                                try:
                                    if dict_of_gears[str(line_num)]:
                                        dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                                except:
                                    dict_of_gears[str(line_num)] = {}
                                    dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                            current_num = ''
                    if current_line[char_index+1] == '*':
                        if added_num == '':
                            print(f'{current_num} is touching *!')
                            added_num = current_num
                            touching_numbers.append(current_num)
                            line_num = i+1
                            star_index = char_index +1
                            try:
                                if dict_of_gears[str(line_num)][str(star_index)]:
                                    dict_of_gears[str(line_num)][str(star_index)].append(current_num)
                            except:
                                try:
                                    if dict_of_gears[str(line_num)]:
                                        dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                                except:
                                    dict_of_gears[str(line_num)] = {}
                                    dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                            current_num = ''
                    if len(prev_line) > 1 and len(next_line) > 1: # ALL DONE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        if prev_line[char_index] == '*':
                            if added_num == '':
                                print(f'{current_num} is touching *!')
                                added_num = current_num
                                touching_numbers.append(current_num)
                                line_num = i
                                star_index = char_index
                                try:
                                    if dict_of_gears[str(line_num)][str(star_index)]:
                                        dict_of_gears[str(line_num)][str(star_index)].append(current_num)
                                except:
                                    try:
                                        if dict_of_gears[str(line_num)]:
                                            dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                                    except:
                                        dict_of_gears[str(line_num)] = {}
                                        dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                                current_num = ''
                        if prev_line[char_index -1] == '*':
                            if added_num == '':
                                print(f'{current_num} is touching *!')
                                added_num = current_num
                                touching_numbers.append(current_num)
                                line_num = i
                                star_index = char_index -1
                                try:
                                    if dict_of_gears[str(line_num)][str(star_index)]:
                                        dict_of_gears[str(line_num)][str(star_index)].append(current_num)
                                except:
                                    try:
                                        if dict_of_gears[str(line_num)]:
                                            dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                                    except:
                                        dict_of_gears[str(line_num)] = {}
                                        dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                                current_num = ''
                        if prev_line[char_index + 1] == '*':
                            if added_num == '':
                                print(f'{current_num} is touching *!')
                                added_num = current_num
                                touching_numbers.append(current_num)
                                line_num = i
                                star_index = char_index + 1
                                try:
                                    if dict_of_gears[str(line_num)][str(star_index)]:
                                        dict_of_gears[str(line_num)][str(star_index)].append(current_num)
                                except:
                                    try:
                                        if dict_of_gears[str(line_num)]:
                                            dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                                    except:
                                        dict_of_gears[str(line_num)] = {}
                                        dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                                current_num = ''
                        if next_line[char_index] == '*':
                            if added_num == '':
                                print(f'{current_num} is touching *!')
                                added_num = current_num
                                touching_numbers.append(current_num)
                                line_num = i+2
                                star_index = char_index
                                try:
                                    if dict_of_gears[str(line_num)][str(star_index)]:
                                        dict_of_gears[str(line_num)][str(star_index)].append(current_num)
                                except:
                                    try:
                                        if dict_of_gears[str(line_num)]:
                                            dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                                    except:
                                        dict_of_gears[str(line_num)] = {}
                                        dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                                current_num = ''
                        if next_line[char_index - 1] == '*':
                            if added_num == '':
                                print(f'{current_num} is touching *!')
                                added_num = current_num
                                touching_numbers.append(current_num)
                                line_num = i+2
                                star_index = char_index -1
                                try:
                                    if dict_of_gears[str(line_num)][str(star_index)]:
                                        dict_of_gears[str(line_num)][str(star_index)].append(current_num)
                                except:
                                    try:
                                        if dict_of_gears[str(line_num)]:
                                            dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                                    except:
                                        dict_of_gears[str(line_num)] = {}
                                        dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                                current_num = ''
                        if next_line[char_index + 1] == '*':
                            if added_num == '':
                                print(f'{current_num} is touching *!')
                                added_num = current_num
                                touching_numbers.append(current_num)
                                line_num = i+2
                                star_index = char_index + 1
                                try:
                                    if dict_of_gears[str(line_num)][str(star_index)]:
                                        dict_of_gears[str(line_num)][str(star_index)].append(current_num)
                                except:
                                    try:
                                        if dict_of_gears[str(line_num)]:
                                            dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                                    except:
                                        dict_of_gears[str(line_num)] = {}
                                        dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                                current_num = ''
                    elif len(prev_line) > 1:
                        if prev_line[char_index] == '*':
                            if added_num == '':
                                print(f'{current_num} is touching *!')
                                added_num = current_num
                                touching_numbers.append(current_num)
                                line_num = i
                                star_index = char_index
                                try:
                                    if dict_of_gears[str(line_num)][str(star_index)]:
                                        dict_of_gears[str(line_num)][str(star_index)].append(current_num)
                                except:
                                    try:
                                        if dict_of_gears[str(line_num)]:
                                            dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                                    except:
                                        dict_of_gears[str(line_num)] = {}
                                        dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                                current_num = ''
                        if prev_line[char_index -1] == '*':
                            if added_num == '':
                                print(f'{current_num} is touching *!')
                                added_num = current_num
                                touching_numbers.append(current_num)
                                line_num = i
                                star_index = char_index - 1
                                try:
                                    if dict_of_gears[str(line_num)][str(star_index)]:
                                        dict_of_gears[str(line_num)][str(star_index)].append(current_num)
                                except:
                                    try:
                                        if dict_of_gears[str(line_num)]:
                                            dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                                    except:
                                        dict_of_gears[str(line_num)] = {}
                                        dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                                current_num = ''
                        if prev_line[char_index + 1] == '*':
                            if added_num == '':
                                print(f'{current_num} is touching *!')
                                added_num = current_num
                                touching_numbers.append(current_num)
                                line_num = i
                                star_index = char_index + 1
                                try:
                                    if dict_of_gears[str(line_num)][str(star_index)]:
                                        dict_of_gears[str(line_num)][str(star_index)].append(current_num)
                                except:
                                    try:
                                        if dict_of_gears[str(line_num)]:
                                            dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                                    except:
                                        dict_of_gears[str(line_num)] = {}
                                        dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                                current_num = ''
                    elif len(next_line) > 1: # ALL DONE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        if next_line[char_index] == '*':
                            if added_num == '':
                                print(f'{current_num} is touching *!')
                                added_num = current_num
                                touching_numbers.append(current_num)
                                line_num = i+2
                                star_index = char_index
                                try:
                                    if dict_of_gears[str(line_num)][str(star_index)]:
                                        dict_of_gears[str(line_num)][str(star_index)].append(current_num)
                                except:
                                    try:
                                        if dict_of_gears[str(line_num)]:
                                            dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                                    except:
                                        dict_of_gears[str(line_num)] = {}
                                        dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                                current_num = ''
                                continue
                        if next_line[char_index - 1] == '*':
                            if added_num == '':
                                print(f'{current_num} is touching *!')
                                added_num = current_num
                                touching_numbers.append(current_num)
                                line_num = i+2
                                star_index = char_index - 1
                                try:
                                    if dict_of_gears[str(line_num)][str(star_index)]:
                                        dict_of_gears[str(line_num)][str(star_index)].append(current_num)
                                except:
                                    try:
                                        if dict_of_gears[str(line_num)]:
                                            dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                                    except:
                                        dict_of_gears[str(line_num)] = {}
                                        dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                                current_num = ''
                                continue
                        if next_line[char_index + 1] == '*':
                            if added_num == '':
                                print(f'{current_num} is touching *!')
                                added_num = current_num
                                touching_numbers.append(current_num)
                                line_num = i+2
                                star_index = char_index + 1
                                try:
                                    if dict_of_gears[str(line_num)][str(star_index)]:
                                        dict_of_gears[str(line_num)][str(star_index)].append(current_num)
                                except:
                                    try:
                                        if dict_of_gears[str(line_num)]:
                                            dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                                    except:
                                        dict_of_gears[str(line_num)] = {}
                                        dict_of_gears[str(line_num)][str(star_index)] = [current_num]
                                current_num = ''
                                continue
                    continue
    ratios = []
    print(dict_of_gears)
    for each_dict in dict_of_gears:
        for each_entry in dict_of_gears[each_dict]:
            if len(dict_of_gears[each_dict][each_entry]) == 2:
                ratios.append(int(dict_of_gears[each_dict][each_entry][0]) * int(dict_of_gears[each_dict][each_entry][1]))
    sum = 0
    for each_ratio in ratios:
        sum += each_ratio
    print(sum)