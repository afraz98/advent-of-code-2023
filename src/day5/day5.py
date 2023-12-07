def solve_part_one(filename):
    input = [line.strip() for line in open(filename, "r")]
    seeds = input[0].split(": ")[1].split(" ")
    pass

print(solve_part_one("day5.txt"))