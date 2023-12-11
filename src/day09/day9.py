def process_differences(line):
    processed_lines = []
    temp = line
    while(temp != [0 for line in range(0, len(line))]):
        temp = [temp[i+1] - temp[i] for i in range(0, len(temp)-1)]
        processed_lines.append(temp)
    return processed_lines

def solve_part_one(filename):
    lines = [[int(value) for value in line.strip("\n").split(" ")] for line in open(filename, "r")]
    processed_lines = [process_differences(line) for line in lines]
    print(processed_lines)


def solve_part_two(filename):
    pass

line = [0, 3, 6, 9, 12, 15]
# print(line)
# line = [line[i+1] - line[i] for i in range(0, len(line)-1)]
# print(line)
# line = [line[i+1] - line[i] for i in range(0, len(line)-1)]
# print(line)

print(process_differences(line))

# solve_part_one("day9_test.txt")