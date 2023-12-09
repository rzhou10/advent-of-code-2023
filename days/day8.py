
def part_one(file):
    with open(file, 'r') as f:
        txt_nodes = f.readlines()

    txt_nodes = list(map(lambda s : s.replace('\n', ''), txt_nodes))

    # store the reading pattern and the node maps as dict
    pattern = txt_nodes[0]
    index = 2
    node_mapping = {}
    current_pattern = 'AAA'

    while index < len(txt_nodes):
        temp = txt_nodes[index].split(" = ")
        temp1 = temp[1].replace('(', '').replace(')', '').split(', ')
        node_mapping[temp[0]] = (temp1[0], temp1[1])
        index += 1
    
    direction_index = 0
    total = 0

    # iterate over each letter in the pattern until we get to ZZZ
    while not current_pattern == "ZZZ":
        # if we hit the end of the pattern start from beginning
        if direction_index == len(pattern):
            direction_index = 0
        if pattern[direction_index] == 'L':
            current_pattern = node_mapping[current_pattern][0]
            total += 1
        elif pattern[direction_index] == 'R':
            current_pattern = node_mapping[current_pattern][1]
            total += 1
        direction_index += 1

    return total