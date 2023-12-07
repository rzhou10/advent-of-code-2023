def part_one(file):
    with open(file, 'r') as f:
        txt_time_and_distance = f.readlines()

    txt_time_and_distance = list(map(lambda s : s.replace('\n', ''), txt_time_and_distance))
    times = txt_time_and_distance[0].split(":")[1].rstrip().split()
    distances = txt_time_and_distance[1].split(":")[1].rstrip().split()

    list_of_combinations = []
    for i in range(len(times)):
        index = 1
        combos = 0
        times_int = int(times[i])
        while index < times_int:
            diff = times_int - index
            if (diff * index > int(distances[i])):
                combos += 1
            index += 1
        list_of_combinations.append(combos)

    return list_of_combinations

def part_two(file):
    with open(file, 'r') as f:
        txt_time_and_distance = f.readlines()

    txt_time_and_distance = list(map(lambda s : s.replace('\n', ''), txt_time_and_distance))
    times = txt_time_and_distance[0].split(":")[1].rstrip().split()
    distances = txt_time_and_distance[1].split(":")[1].rstrip().split()
    temp = ''
    temp1 = ''

    for i in range(len(times)):
        temp += times[i]
        temp1 += distances[i]
    total_time = int(temp)
    total_distance = int(temp1)

    index = 1
    combos = 0
    while index < total_time:
        diff = total_time - index
        if (diff * index > total_distance):
            combos += 1
        index += 1

    return combos