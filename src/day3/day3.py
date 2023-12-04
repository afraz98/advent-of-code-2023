def solve_part_one(filename):
    input = [[char for char in line.strip("\r\n")] for line in open(filename, 'r')]
    print(input)

solve_part_one("day3_test.txt")