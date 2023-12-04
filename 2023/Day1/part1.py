with open('Day1\Part1\input.txt', 'r') as input:
    final_values = []
    for line in input:
        int_in_str = []
        string = str(line)
        for char in string:
            if char.isdigit():
                int_in_str.append(int(char))
        final_values.append(str(int_in_str[0]) +  str(int_in_str[-1]))
    sum = 0
    for each_value in final_values:
        sum += int(each_value)