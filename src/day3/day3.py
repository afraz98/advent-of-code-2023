def find_symbols(map):
    symbols = []
    for row in range(0, len(map)):
        for column in range(0, len(map[0])):
            if map[row][column] not in "0123456789" and map[row][column] != ".":
                symbols.append((map[row][column], row, column))
    return symbols

def find_part_numbers(map):
    pass

def solve_part_one(filename):
    map = [[char for char in line.strip("\r\n")] for line in open(filename, 'r')]
    symbols = find_symbols(map)
    print(symbols)
    return -1

print(solve_part_one("day3.txt"))