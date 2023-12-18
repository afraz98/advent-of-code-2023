def calculate_load(map, rock):
    return len(map) - rock[0]

def display_map(map):
    for i in range(0, len(map)):
        print(''.join(map[i]))

def tilt_rocks_up(map, round_rocks):
    for i in range(len(round_rocks)):
        rock_y, rock_x = round_rocks[i]
        while rock_y > 0 and map[rock_y - 1][rock_x] == ".":
            map[rock_y][rock_x] = "."
            rock_y = rock_y - 1
        
        round_rocks[i] = (rock_y, rock_x)
        map[rock_y][rock_x] = 'O'

def tilt_rocks_down(map, round_rocks):
    for i in reversed(range(len(round_rocks))):
        rock_y, rock_x = round_rocks[i]
        while rock_y < len(map)-1 and map[rock_y + 1][rock_x] == ".":
            map[rock_y][rock_x] = "."
            rock_y = rock_y + 1
    
        round_rocks[i] = (rock_y, rock_x)
        map[rock_y][rock_x] = 'O'

def tilt_rocks_left(map, round_rocks):
    for i in range(len(round_rocks)):
        rock_y, rock_x = round_rocks[i]
        while rock_x > 0 and map[rock_y][rock_x - 1] == ".":
            map[rock_y][rock_x] = "."
            rock_x = rock_x - 1
    
        round_rocks[i] = (rock_y, rock_x)
        map[rock_y][rock_x] = 'O'

def tilt_rocks_right(map, round_rocks):
    for i in reversed(range(len(round_rocks))):
        rock_y, rock_x = round_rocks[i]
        while rock_x < len(map[0])-1 and map[rock_y][rock_x + 1] == ".":
            map[rock_y][rock_x] = "."
            rock_x = rock_x + 1
    
        round_rocks[i] = (rock_y, rock_x)
        map[rock_y][rock_x] = 'O'

def solve_part_one(filename):
    map = [[character for character in line.strip('\n')] for line in open(filename, 'r')]
    
    round_rocks = []
    for row in range(len(map)):
        for col in range(0, len(map[0])):
            if map[row][col] == "O":
                round_rocks.append((row, col))

    tilt_rocks_up(map, round_rocks)    
    display_map(map)
    return sum([calculate_load(map, rock) for rock in round_rocks])

# Work in progress
def solve_part_two(filename):
    map = [[c for c in line.strip('\n')] for line in open(filename, 'r')]
    
    round_rocks = []
    for row in range(len(map)):
        for col in range(0, len(map[0])):
            if map[row][col] == "O":
                round_rocks.append((row, col))
    
    # NWSE    
    tilt_rocks_up(map, round_rocks)
    display_map(map)
    print()

    tilt_rocks_left(map, round_rocks)
    display_map(map)
    print()
    
    tilt_rocks_down(map, round_rocks)
    display_map(map)
    print()

    tilt_rocks_right(map, round_rocks)
    display_map(map)
    print()

    return sum([calculate_load(map, rock) for rock in round_rocks])

# print(solve_part_one("day14_test.txt"))
print(solve_part_two("day14_test.txt"))
