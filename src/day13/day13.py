def parse_input(filename):
    return [[c for c in line.strip('\n')] for line in open(filename, 'r')]

def find_reflection_rows(map):
    for i in range(1, len(map)):
        if map[i] == map[i-1]:
            if all([map[i+j] == map[i-1-j] for j in range(i-len(map))]):
                return i+1
    return 0

def find_reflection_columns(map):
    for i in range(1, len(map[0])):
        if [map[x][i-1] for x in range(len(map))] == [map[x][i] for x in range(len(map))]:
            print(i)
            if all([[map[x][i-1+j] for x in range(len(map))] == [map[x][i-j] for x in range(len(map))] for j in range(i-len(map[0]))]):
                return i
    return 0

def solve_part_one(filename):
    map = parse_input(filename)
    return 100 * find_reflection_rows(map) + find_reflection_columns(map)

def solve_part_two(filename):
    pass

print(solve_part_one("day13_test.txt"))

