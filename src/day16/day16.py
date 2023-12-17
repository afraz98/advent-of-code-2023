def parse_input(filename):
    return [[c for c in line.strip('\n')] for line in open(filename, 'r')]

def print_map(map):
    for row in range(len(map)):
        print(map[row])
    pass

def solve_part_one(filename):
    map = parse_input(filename)
    print_map(map)

def solve_part_two(filename):
    map = parse_input(filename)

solve_part_one("day16_test.txt")
solve_part_two("day16_test.txt")
