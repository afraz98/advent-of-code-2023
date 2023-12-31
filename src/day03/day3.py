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
    number_coordinates = set()
    for row in range(0, len(map)):
        for column in range(0, len(map[0])):
            if map[row][column] in "0123456789":
                number += map[row][column]
                number_coordinates.add((row, column))
            if(map[row][column] not in "0123456789") or column == len(map[0])-1: # End of line or non-digit character reached
                if number != "":
                    numbers.append((int(number), number_coordinates))
                number_coordinates = set()
                number = ""
    return numbers

def adjacent_coordinates(x, y):
    return [(x, y+1), (x, y-1), (x+1, y), (x-1, y), (x-1, y-1), (x+1, y+1), (x+1,y-1), (x-1, y+1)]

def find_numbers_with_symbols_adjacent(part_numbers, symbols):
    numbers = []
    for symbol in symbols:
        _, symbol_x, symbol_y = symbol
        for number in part_numbers:
            number, coordinates = number
            if any([coord in adjacent_coordinates(symbol_x, symbol_y) for coord in coordinates]):
                numbers.append(number)        
    return numbers

def solve_part_one(filename):
    map = [[char for char in line.strip("\r\n")] for line in open(filename, 'r')]
    return sum([int(part_number) for part_number in find_numbers_with_symbols_adjacent(find_part_numbers(map), find_symbols(map))])

def find_gears(map):
    gears = []
    for row in range(0, len(map)):
        for column in range(0, len(map[0])):
            if map[row][column] == "*":
                gears.append((map[row][column], row, column))
    return gears

def find_gear_ratios(part_numbers, gears):
    gear_ratios = []
    for gear in gears:
        gear_ratio = 1
        ratios = []
        _, gear_x, gear_y = gear
        for number in part_numbers:
            number, coordinates = number
            
            if any([coord in adjacent_coordinates(gear_x, gear_y) for coord in coordinates]):
                ratios.append(number)
            
        if len(ratios) > 1:
            for ratio in ratios:
                gear_ratio *= ratio
            gear_ratios.append(gear_ratio)
    return gear_ratios

def solve_part_two(filename):
    map = [[char for char in line.strip("\r\n")] for line in open(filename, 'r')]
    return sum([int(part_number) for part_number in find_gear_ratios(find_part_numbers(map), find_gears(map))])

print(solve_part_one("day3.txt"))
print(solve_part_two("day3.txt"))