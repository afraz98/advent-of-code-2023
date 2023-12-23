def parse_input(filename):
    return [[row for row in map.split('\n')] for map in open(filename, 'r').read().split('\n\n')]

def find_reflection_rows(map):
    for i in range(1, len(map)):
        if map[i] == map[i-1]:
            if all([map[i+j] == map[i-1-j] for j in range(len(map)-i)]):
                print("Row %d" % (i))
                return i
    return 0

def find_reflection_columns(map):
    for i in range(1, len(map[0])):
        if [map[x][i-1] for x in range(len(map))] == [map[x][i] for x in range(len(map))]:
            if all([[map[x][i-1-j] for x in range(len(map))] == [map[x][i+j] for x in range(len(map))] for j in range(len(map[0])-i)]):
                print("Column %d" % i)
                return i
    return 0

def solve_part_one(filename):
    return sum([(100*find_reflection_rows(map)) + find_reflection_columns(map) for map in parse_input(filename)])

print(solve_part_one("day13_test.txt"))

