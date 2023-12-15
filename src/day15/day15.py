def HASH(part):
    value = 0
    for character in part:
        value += ord(character)
        value *= 17
        value = value % 256
    return value

print(HASH("HASH"))

def solve_part_one(filename):
    sequence = [line.strip('\n') for line in open(filename, 'r')][0].split(",")
    return sum([HASH(x) for x in sequence])

def solve_part_two(filename):
    pass

print(solve_part_one("day15.txt"))