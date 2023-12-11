def map_value(value, mappings):
    for sources, destinations in mappings:
        if value in sources:
            return destinations[sources.index(value)]
    return value

def consume(input_lines):
    if(input_lines[0] == "\n"):
        input_lines = input_lines[1:]

def parse_next_map(input):
    mappings = []
    while(input[0] != "\n"):
        dest_start, src_start, step = [int(number) for number in input[0].strip("\n").split(" ")]
        mappings.append((range(src_start, src_start + step), range(dest_start, dest_start + step)))
        input = input[1:]
    return mappings, input

def solve_part_one(filename):
    input = [line for line in open(filename, "r")]
    values = [int(seed) for seed in input[0].strip("\n").split(": ")[1].split(" ")]
    input = input[1:]

    mappings = []   
    input = input[2:]

    while(input):
        mappings, input = parse_next_map(input)
        values = [map_value(value, mappings) for value in values]
        input = input[2:]

    return min(values)

print(solve_part_one("day5_test.txt"))

