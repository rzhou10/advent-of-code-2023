def part1(file):
    with open(file, 'r') as f:
        txt_nums = f.readlines()

    txt_nums = list(map(lambda s : s.replace('\n', ''), txt_nums))

    list_of_nums = []
    for code in txt_nums:
        temp = ""
        # check if the character is a valid number
        # pt 2 also check if the string is a valid number
        for character in code:
            if character.isdigit():
                temp += character
                break
        reversed_code = code[::-1]
        for character1 in reversed_code:
            if character1.isdigit():
                temp += character1
                break
        list_of_nums.append(int(temp))
    return list_of_nums

def part2(file):
    with open(file, 'r') as f:
        txt_nums = f.readlines()

    txt_nums = list(map(lambda s : s.replace('\n', ''), txt_nums))

    list_of_nums = []
    for code in txt_nums:
        temp = ""
        # check if the character is a valid number
        # pt 2 also check if the string is a valid number
        for index, character in enumerate(code):
            if character.isdigit():
                temp += character
                break
            elif code.startswith("one", index):
                temp += "1"
                break
            elif code.startswith("two", index):
                temp += "2"
                break
            elif code.startswith("three", index):
                temp += "3"
                break
            elif code.startswith("four", index):
                temp += "4"
                break
            elif code.startswith("five", index):
                temp += "5"
                break
            elif code.startswith("six", index):
                temp += "6"
                break
            elif code.startswith("seven", index):
                temp += "7"
                break
            elif code.startswith("eight", index):
                temp += "8"
                break
            elif code.startswith("nine", index):
                temp += "9"
                break
        reversed_code = code[::-1]
        for index1, character1 in enumerate(reversed_code):
            if character1.isdigit():
                temp += character1
                break
            elif reversed_code.startswith("eno", index1):
                temp += "1"
                break
            elif reversed_code.startswith("owt", index1):
                temp += "2"
                break
            elif reversed_code.startswith("eerht", index1):
                temp += "3"
                break
            elif reversed_code.startswith("ruof", index1):
                temp += "4"
                break
            elif reversed_code.startswith("evif", index1):
                temp += "5"
                break
            elif reversed_code.startswith("xis", index1):
                temp += "6"
                break
            elif reversed_code.startswith("neves", index1):
                temp += "7"
                break
            elif reversed_code.startswith("thgie", index1):
                temp += "8"
                break
            elif reversed_code.startswith("enin", index1):
                temp += "9"
                break
        list_of_nums.append(int(temp))
    return list_of_nums