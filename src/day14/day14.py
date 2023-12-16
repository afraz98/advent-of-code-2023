def calculate_load(map, rock):
    return len(map) - rock[0]

def solve_part_one(filename):
    map = [[character for character in line.strip('\n')] for line in open(filename, 'r')]
    
    round_rocks = []
    for row in range(len(map)):
        for col in range(0, len(map[0])):
            if map[row][col] == "O":
                round_rocks.append((row, col))

    square_rocks = []
    for row in range(len(map)):
        for col in range(0, len(map[0])):
            if map[row][col] == "#":
                square_rocks.append((row, col))
    
    for i in range(len(round_rocks)):
        rock_y, rock_x = round_rocks[i]
        while rock_y > 0 and map[rock_y - 1][rock_x] == ".":
            map[rock_y][rock_x] = "."
            rock_y = rock_y - 1
        
        round_rocks[i] = (rock_y, rock_x)
        map[rock_y][rock_x] = 'O'

    return sum([calculate_load(map, rock) for rock in round_rocks])

def solve_part_two(filename):
    return 0

print(solve_part_one("day14.txt"))
print(solve_part_two("day14_test.txt"))
