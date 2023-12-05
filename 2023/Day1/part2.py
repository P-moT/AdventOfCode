with open('2023\Day1\input.txt', 'r') as input:
    final_values = []
    for line in input:
        int_in_str = []
        string = str(line)
        string2 = (string.replace("one", "one1one")
                .replace("two","two2two")
                .replace("three","three3three")
                .replace("four","four4four")
                .replace("five","five5five")
                .replace("six","six6six")
                .replace("seven","seven7seven")
                .replace("eight", "eight8eight")
                .replace("nine","nine9nine")
        )
        for char in string2:
            if char.isdigit():
                int_in_str.append(int(char))
        final_values.append(str(int_in_str[0]) +  str(int_in_str[-1]))
    sum = 0
    for each_value in final_values:
        sum += int(each_value)
    print(sum)