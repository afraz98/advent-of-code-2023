def parse_input(filename):
    return [[[character for character in row] for row in map.split('\n')] for map in open(filename, 'r').read().split('\n\n')]

def count_differences(str1, str2):
    # From here: https://stackoverflow.com/questions/28423448/counting-differences-between-two-strings
    return sum(1 for a, b in zip(str1, str2) if a != b)

def find_reflections(map):
    # First check horizontal lines (row splits)
    for i in range(1, len(map)):
        if all([map[i+j] == map[i-1-j] for j in range(min(len(map)-i, i))]):
            return 100 * i

    # Next check vertical lines (column splits)
    for i in range(1, len(map[0])):
        if all([[map[x][i-1-j] for x in range(len(map))] == [map[x][i+j] for x in range(len(map))] for j in range(min(len(map[0])-i, i))]):
            return i
    return 0

def solve_part_one(filename):
    return sum(find_reflections(map) for map in parse_input(filename))

def fix_smudges(maps):
    for map in maps:
        # First check horizontal lines (row splits)
        for i in range(1, len(map)):
            if count_differences(map[i-1], map[i]) == 1:
                map[i] = map[i-1]

        for i in range(1, len(map)):
            for j in range(min(len(map)-i, i)):
                if count_differences(map[i+j], map[i-1-j]) == 1:
                        map[i+j] = map[i-1-j]

        # Next check vertical lines (column) splits
        for i in range(1, len(map[0])):
            if count_differences([map[x][i-1] for x in range(len(map))], [map[x][i] for x in range(len(map))]) == 1:
                for x in range(len(map)):
                    map[x][i-1] = map[x][i]

        for i in range(1, len(map[0])):
            for j in range(min(len(map[0])-i, i)):
                if count_differences([map[x][i-1-j] for x in range(len(map))], [map[x][i+j] for x in range(len(map))]) == 1:
                    for x in range(len(map)):
                        map[x][i-1-j] = map[x][i+j]


    return maps

# 37813?
# 37282?
def solve_part_two(filename):
    return sum(find_reflections(map) for map in fix_smudges(parse_input(filename)))

print(solve_part_one("day13.txt"))
print(solve_part_two("day13.txt"))
