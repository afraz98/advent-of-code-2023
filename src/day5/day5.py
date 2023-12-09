def convert_value(value, mappings):
    for sources, destinations in mappings:
        if value in sources:
            return destinations[sources.index(value)]
    return value

def convert_value_ranges():
    pass

def parse_next_map(input):
    mappings = []
    while(input[0] != "\n"):
        dest_start, src_start, step = [int(number) for number in input[0].strip("\n").split(" ")]
        mappings.append((range(src_start, src_start + step), range(dest_start, dest_start + step)))
        input = input[1:]
    return mappings, input

def solve_part_one(filename):
    input = [line for line in open(filename, "r")]
    
    # Process the list of seeds
    values = [int(seed) for seed in input[0].strip("\n").split(": ")[1].split(" ")]
    input = input[1:]

    mappings = []   
    input = input[2:]

    while(input):
        mappings, input = parse_next_map(input)
        values = [convert_value(seed, mappings) for seed in values]
        input = input[2:]

    return min(values)

# Work in progress
# This could probably be optimized but I'm tired
def solve_part_two(filename):
    input = [line for line in open(filename, "r")]

    ranges = [int(val) for val in input[0].strip("\n").split(": ")[1].split(" ")]
    value_ranges = []
    # Process the list of seeds
    for i in range(0, len(ranges)-1):
        value_ranges.append(range(ranges[i], ranges[i+1]))
    input = input[1:]

    mappings = []   
    input = input[2:]

    while(input):
        mappings, input = parse_next_map(input)
        value_ranges = [convert_value(seed, mappings) for seed in value_ranges]
        input = input[2:]

    return min(value_ranges)

print(solve_part_one("day5.txt"))
print(solve_part_two("day5.txt"))