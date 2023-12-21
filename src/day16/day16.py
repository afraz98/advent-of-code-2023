def parse_input(filename):
    return [[c for c in line] for line in open(filename, 'r').read().splitlines()]

def print_map(map):
    for row in range(len(map)):
        print(''.join(map[row]))
    pass

def traverse_map(x, y, dx, dy, map):

    if x < 0 or x >= len(map[0]):
        return 0
    
    if y < 0 or y >= len(map):
        return 0

    print(y, x, dx, dy)
    print(map[y][x])

    if map[y][x] == ".":
        return 1 + traverse_map(x + dx, y + dy, dx, dy, map)

    if map[y][x] == "-":
        if dy != 0: # Approaching from top/bottom
            return 1 + traverse_map(x + 1, y, 1, 0, map) + traverse_map(x-1, y, 1, 0, map)
        else:       # Continue as normal
            return 1 + traverse_map(x + dx, y + dy, dx, dy, map)
    
    if map[y][x] == "|":
        if dx != 0: # Approaching from either side
            return 1 + traverse_map(x, y+1, 0, 1, map) + traverse_map(x, y-1, 0, -1, map)
        else:       # Continue as normal
            return 1 + traverse_map(x + dx, y + dy, dx, dy, map)    
    
    if map[y][x] == "\\":
        if dx > 0:
            return 1 + traverse_map(x, y + 1, 0, 1, map)
        if dx < 0:
            return 1 + traverse_map(x, y - 1, 0, -1, map)
        if dy > 0:
            return 1 + traverse_map(x + 1, y, 1, 0, map)
        else:
            return 1 + traverse_map(x - 1, y, -1, 0, map)
        
    if map[y][x] == "/":
        if dx > 0:
            return 1 + traverse_map(x, y - 1, 0, -1, map)
        if dx < 0:
            return 1 + traverse_map(x, y + 1, 0, 1, map)
        if dy > 0:
            return 1 + traverse_map(x - 1, y, -1, 0, map)
        if dy < 0:
            return 1 + traverse_map(x + 1, y, 1, 0, map)
    
    return 0

def solve_part_one(filename):
    map = parse_input(filename)
    print_map(map)

    return traverse_map(0, 0, 1, 0, map)

def solve_part_two(filename):
    map = parse_input(filename)

print(solve_part_one("day16_test.txt"))
