def parse_input(filename):
    return [[row for row in map.split('\n')] for map in open(filename, 'r').read().split('\n\n')]

def find_reflections(map):
    # First check horizontal lines (row splits)
    for i in range(1, len(map)):
        if all([map[i+j] == map[i-1-j] for j in range(len(map)-i)]):
            return 100 * i

    # Next check vertical lines (column splits)
    for i in range(1, len(map[0])):
        if all([[map[x][i-1-j] for x in range(len(map))] == [map[x][i+j] for x in range(len(map))] for j in range(len(map[0])-i)]):
            return i
            
    # No reflections found
    return 0

def solve_part_one(filename):
    return sum(find_reflections(map) for map in parse_input(filename))

print(solve_part_one("day13.txt"))

