def parse_input(filename):
    return [[[character for character in row] for row in map.split('\n')] for map in open(filename, 'r').read().split('\n\n')]

def count_differences(str1, str2):
    # From here: https://stackoverflow.com/questions/28423448/counting-differences-between-two-strings
    return sum(1 for a, b in zip(str1, str2) if a != b)

def find_reflections(map, mismatches):
    # First check horizontal lines (row splits)
    for i in range(1, len(map)):
        if sum([count_differences(map[i+j],map[i-1-j]) for j in range(min(len(map)-i, i))]) == mismatches:
            return 100 * i

    # Transpose map
    map = [*zip(*map)]

    # Next check vertical lines (column splits)
    for i in range(1, len(map)):
        if sum([count_differences(map[i+j],map[i-1-j]) for j in range(min(len(map)-i, i))]) == mismatches:
            return i        
    return 0

def solve_part_one(filename):
    return sum(find_reflections(map, 0) for map in parse_input(filename))

def solve_part_two(filename):
    return sum(find_reflections(map, 1) for map in parse_input(filename))

print(solve_part_one("day13.txt"))
print(solve_part_two("day13.txt"))
