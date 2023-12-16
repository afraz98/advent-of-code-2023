def HASH(part):
    value = 0
    for character in part:
        value += ord(character)
        value *= 17
        value = value % 256
    return value

def execute_command(command, maps):
    print(command)
    if '-' in command:
        command = command.split('-')
        box = HASH(command[0])
        if command[0] in maps[box].keys():
            maps[box].pop(command[0])
    if '=' in command:
        command = command.split('=')
        box = HASH(command[0])
        maps[box][command[0]] = int(command[1])
    pass

def solve_part_one(filename):
    sequence = [line.strip('\n') for line in open(filename, 'r')][0].split(",")
    return sum([HASH(x) for x in sequence])

def solve_part_two(filename):
    boxes = [{} for i in range(0, 256)]
    sequence = [line.strip('\n') for line in open(filename, 'r')][0].split(",")
    for command in sequence:
        execute_command(command, boxes)
    
    sum = 0
    for i in range(0, len(boxes)):
        for j, key in enumerate(boxes[i].keys()):
            sum += (i + 1) * (j+1) * boxes[i][key]
    return sum

print(solve_part_one("day15.txt"))
print(solve_part_two("day15.txt"))
