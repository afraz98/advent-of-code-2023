def process_differences(line):
    processed_lines = [line]
    temp = line
    
    while(not all([temp[i] == 0 for i in range(0, len(temp))])):
        temp = [temp[i+1] - temp[i] for i in range(0, len(temp)-1)]
        processed_lines.append(temp)
    return processed_lines

def extrapolate_value(processed_differences):
    for index in list(reversed(range(0, len(processed_differences)))):
        if(index == len(processed_differences)-1):
            processed_differences[index].append(0)
        else:
            processed_differences[index].append(processed_differences[index+1][-1] + processed_differences[index][-1])
    return processed_differences[0][-1]

def solve_part_one(filename):
    extrapolated_values = []
    lines = [[int(value) for value in line.strip("\n").split(" ")] for line in open(filename, "r")]    
    for line in lines:
        processed_differences = process_differences(line)
        extrapolated_values.append(extrapolate_value(processed_differences))
    return sum(extrapolated_values)

def solve_part_two(filename):
    pass

print(solve_part_one("day9.txt"))