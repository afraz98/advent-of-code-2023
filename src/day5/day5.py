def convert_value(value, mappings):
    for sources, destinations in mappings:
        if value in sources:
            return destinations[sources.index(value)]
    return value

def parse_next_map(input):
    mappings = []
    while(input[0] != "\n"):
        dest_start, src_start, step = [int(number) for number in input[0].strip("\n").split(" ")]
        mappings.append((list(range(src_start, src_start + step)), list(range(dest_start, dest_start + step))))
        input = input[1:]
    return mappings, input

def solve_part_one(filename):
    input = [line for line in open(filename, "r")]
    
    # Process the list of seeds
    values = [int(seed) for seed in input[0].strip("\n").split(": ")[1].split(" ")]
    input = input[1:]

    mappings = []   
    input = input[2:]

    # Process seed to soil map
    mappings, input = parse_next_map(input)
    values = [convert_value(seed, mappings) for seed in values]
    input = input[2:]

    # Process soil to fertilizer map
    mappings, input = parse_next_map(input)
    values = [convert_value(soil, mappings) for soil in values]
    input = input[2:]

    # Process fertilizer to water map
    mappings, input = parse_next_map(input)
    values = [convert_value(fertilizer, mappings) for fertilizer in values]
    input = input[2:]

    # Process water to light map
    mappings, input = parse_next_map(input)
    values = [convert_value(water, mappings) for water in values]
    input = input[2:]

    # Process light to temperature map
    mappings, input = parse_next_map(input)
    values = [convert_value(light, mappings) for light in values]
    input = input[2:]

    # Process temperature to humidity map
    mappings, input = parse_next_map(input)
    values = [convert_value(temperature, mappings) for temperature in values]
    input = input[2:]

    # Process humidity to location map
    mappings, input = parse_next_map(input)
    values = [convert_value(humidity, mappings) for humidity in values]
    input = input[2:]

    return min(values)

print(solve_part_one("day5_test.txt"))