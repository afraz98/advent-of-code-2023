def find_symbols(map):
    symbols = []
    for row in range(0, len(map)):
        for column in range(0, len(map[0])):
            if map[row][column] not in "0123456789" and map[row][column] != ".":
                symbols.append((map[row][column], row, column))
    return symbols

def find_part_numbers(map):
    numbers = []
    number = ""
    for row in range(0, len(map)):
        for column in range(0, len(map[0])):
            if map[row][column] in "0123456789":
                number += map[row][column]
            if(map[row][column] == "."):
                numbers.append(number)
                number = ""
    return list(filter(lambda x: x != '', [number if number != '' else '' for number in numbers]))

def find_numbers_with_symbols_adjacent(part_numbers, symbols):
    return []

def solve_part_one(filename):
    map = [[char for char in line.strip("\r\n")] for line in open(filename, 'r')]
    return sum([int(part_number) for part_number in find_numbers_with_symbols_adjacent(find_part_numbers(map), find_symbols(map))])

print(solve_part_one("day3.txt"))