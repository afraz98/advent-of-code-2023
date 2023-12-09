def map_value(value, mappings):
    for sources, destinations in mappings:
        if value in sources:
            return destinations[sources.index(value)]
    return value

def map_value_range(value_range, mappings, value_ranges):
    """
    Map each value range to the corresponding output, separating ranges into multiple ranges 
    if portions of the range do not fit within the mapping.

    e.g. if one of the mappings is 52 50 48, this corresponds to range(50, 98) and range(52, 100):
        (case 1) If the value range is (79,14), this corresponds to range(79, 14) becoming (81,4) which is (79+(52 - 50), 4)
        (case 2) If the value range is (45,11), we know that (45,5) does not fit into the list, but (50, 6) does so it becomes (52, 6)

    Args:
        value_range (range): Range of values to be mapped
        mappings (list): List of destination ranges with associated source ranges
    Returns:
        (list): value_ranges with newly-mapped start and step values
    """
    start_value, step_value = value_range
    for map_src_start, step, map_dest_start in mappings:
        if map_src_start < start_value:
            value_ranges.append((start_value + abs(map_dest_start - map_src_start), step_value))
            return value_ranges
        else:
            value_ranges.append((start_value, (map_src_start - start_value)))

            # Append remainder of input
            value_ranges.append((map_src_start + abs(map_dest_start - map_src_start), (step_value - (map_src_start - start_value))))
            return value_ranges
    return value_ranges

assert map_value_range((79,14), [(50, 48, 52)], []) == [(81,14)]
assert map_value_range((45,11), [(50, 48, 52)], []) == [(45,5), (52,6)]

def parse_next_map(input):
    mappings = []
    while(input[0] != "\n"):
        dest_start, src_start, step = [int(number) for number in input[0].strip("\n").split(" ")]
        mappings.append((range(src_start, src_start + step), range(dest_start, dest_start + step)))
        input = input[1:]
    return mappings, input

def parse_next_map_for_range(input):
    mappings = []
    while(input[0] != "\n"):
        dest_start, src_start, step = [int(number) for number in input[0].strip("\n").split(" ")]
        mappings.append((src_start, step, dest_start))
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

def solve_part_two(filename):
    input = [line for line in open(filename, "r")]
    ranges = [int(val) for val in input[0].strip("\n").split(": ")[1].split(" ")]
    value_ranges = [(ranges[i], ranges[i+1]) for i in range(0, len(ranges)-1)]
    input = input[1:]

    mappings = []   
    input = input[2:]

    while(input):
        mappings, input = parse_next_map_for_range(input)
        new_ranges = []
        for r in value_ranges:
            new_ranges = map_value_range(r, mappings, new_ranges)
        value_ranges = new_ranges
        input = input[2:]

    return sorted(value_ranges, key=lambda x: x[0])[0][0]

assert solve_part_one("day5_test.txt") == 35
assert solve_part_two("day5_test.txt") == 14

print(solve_part_one("day5.txt"))
print(solve_part_two("day5.txt"))