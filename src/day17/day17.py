def parse_input(filename):
    return [[character for character in line.strip('\n')] for line in open(filename, 'r')]

def print_maze(maze):
    for i in range(len(maze)):
        print(''.join(maze[i]))

def solve_part_one(filename):
    maze = parse_input(filename)
    print_maze(maze)
    return 0

print(solve_part_one("day17_test.txt"))