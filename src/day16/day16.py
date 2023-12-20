def parse_input(filename):
    return [[c for c in line] for line in open(filename, 'r').read().splitlines()]

def print_map(map):
    for row in range(len(map)):
        print(''.join(map[row]))
    pass

def traverse_map(x, y, x_prev, y_prev, map):
    if x < 0 or x >= len(map[0]):
        return 0
    
    if y < 0 or x >= len(map):
        return 0

    if map[y][x] == "." and x == 0 and y == 0:
        return 1 + traverse_map(x+1, y, x, y, map)
    
    if map[y][x] == "-": 
        if y_prev == y - 1 or y_prev == y + 1:
            return 1 + traverse_map(x-1, y, x, y, map) + traverse_map(x+1, y, x, y, map)

    if map[y][x] == "|" and (x_prev == x - 1 or x_prev == x + 1):
        return 1 + traverse_map(x, y+1, x, y, map) + traverse_map(x, y-1, x, y, map)
    
    return 0

def solve_part_one(filename):
    map = parse_input(filename)
    print_map(map)
    return traverse_map(0, 0, 0, 0, map)

def solve_part_two(filename):
    map = parse_input(filename)

print(solve_part_one("day16_test.txt"))
