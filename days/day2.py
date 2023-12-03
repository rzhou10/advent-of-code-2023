def part_one(file):
    with open(file, 'r') as f:
        txt_games = f.readlines()

    txt_games = list(map(lambda s : s.replace('\n', ''), txt_games))

    list_of_valid_games = []
    
    for game in txt_games:
        # split the games and also find the id
        rounds = game.split(";")
        temp = rounds[0].split(":")
        rounds[0] = temp[1].strip()
        game_id = temp[0].split(" ")[1]

        is_valid = True

        for r in rounds:
            temp1 = r.strip().split(',')
            for cube in temp1:
                # check the color of the cube and make sure it's less than the valid number of cubes
                if "red" in cube and not int(cube.strip().split(" ")[0]) <= 12:
                    is_valid = False
                    break
                if "green" in cube and not int(cube.strip().split(" ")[0]) <= 13:
                    is_valid = False
                    break
                if "blue" in cube and not int(cube.strip().split(" ")[0]) <= 14:
                    is_valid = False
                    break

        if is_valid:
            list_of_valid_games.append(int(game_id))
    return list_of_valid_games

def part_two(file):
    with open(file, 'r') as f:
        txt_games = f.readlines()

    txt_games = list(map(lambda s : s.replace('\n', ''), txt_games))
    multiple_of_maxes = []
    
    for game in txt_games:
        # split the games and also find the id
        rounds = game.split(";")
        temp = rounds[0].split(":")
        rounds[0] = temp[1].strip()

        max_red_cubes = 0
        max_green_cubes = 0
        max_blue_cubes = 0

        for r in rounds:
            temp1 = r.strip().split(',')
            for cube in temp1:
                num = int(cube.strip().split(" ")[0])
                # check the color of the cube and and add to max if it's greater
                if "red" in cube and num > max_red_cubes:
                    max_red_cubes = num
                if "green" in cube and num > max_green_cubes:
                    max_green_cubes = num
                if "blue" in cube and num > max_blue_cubes:
                    max_blue_cubes = num
                    
        multiple_of_maxes.append(max_red_cubes * max_green_cubes * max_blue_cubes)
    
    return multiple_of_maxes
