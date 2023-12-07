# build the mapping required
def build_range_mapping(txt_seed_info, index):
    [destination, start, map_range] = txt_seed_info[index].split()
    destination1 = int(destination)
    start1 = int(start)
    map_range1 = int(map_range)
    first_range = {}

    for i in range(map_range1):
        first_range[start1] = destination1
        destination1 += 1
        start1 += 1
    
    return first_range

# this isn't efficient enough, will have to look into this
def part_one(file):
    with open(file, 'r') as f:
        txt_seed_info = f.readlines()

    txt_seed_info = list(map(lambda s : s.replace('\n', ''), txt_seed_info))
    txt_seed_info = list(filter(lambda s : s.rstrip(), txt_seed_info))

    seed_info_dict = {}
    # get the seeds and add to dict
    temp = txt_seed_info[0].split()
    for s in temp:
        if s.isdigit():
            seed_info_dict[s] = [0, 0, 0, 0, 0, 0, 0]


    index = 1
    while index < len(txt_seed_info):
        total_range = {}
        name = ""
        if not txt_seed_info[index][0].isdigit():
            name = txt_seed_info[index]
            index += 1
        while index < len(txt_seed_info) and txt_seed_info[index][0].isdigit():
            # merge dict to get total ranges
            total_range = total_range | build_range_mapping(txt_seed_info, index)
            index += 1

        # based on the maps, find which numbers correlate with each other
        if name == "seed-to-soil map:":
            for seed in seed_info_dict:
                seed_info_dict[seed][0] = total_range[int(seed)] if int(seed) in total_range.keys() else int(seed)
        elif name == "soil-to-fertilizer map:":
            for seed in seed_info_dict:
                seed_info_dict[seed][1] = total_range[seed_info_dict[seed][0]] if seed_info_dict[seed][0] in total_range.keys() else seed_info_dict[seed][0]
        elif name == "fertilizer-to-water map:":
            for seed in seed_info_dict:
                seed_info_dict[seed][2] = total_range[seed_info_dict[seed][1]] if seed_info_dict[seed][1] in total_range.keys() else seed_info_dict[seed][1]
        elif name == "water-to-light map:":
            for seed in seed_info_dict:
                seed_info_dict[seed][3] = total_range[seed_info_dict[seed][2]] if seed_info_dict[seed][2] in total_range.keys() else seed_info_dict[seed][2]
        elif name == "light-to-temperature map:":
            for seed in seed_info_dict:
                seed_info_dict[seed][4] = total_range[seed_info_dict[seed][3]] if seed_info_dict[seed][3] in total_range.keys() else seed_info_dict[seed][3]
        elif name == "temperature-to-humidity map:":
            for seed in seed_info_dict:
                seed_info_dict[seed][5] = total_range[seed_info_dict[seed][4]] if seed_info_dict[seed][4] in total_range.keys() else seed_info_dict[seed][4]
        elif name == "humidity-to-location map:":
            for seed in seed_info_dict:
                seed_info_dict[seed][6] = total_range[seed_info_dict[seed][5]] if seed_info_dict[seed][5] in total_range.keys() else seed_info_dict[seed][5]
    
    locations = map(lambda x: seed_info_dict[x][6], seed_info_dict)
    return min(locations)


print(part_one("../inputs/day5/day5.txt"))