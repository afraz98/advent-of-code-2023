def parse_input(filename):
    return [[character for character in line] for line in open(filename, 'r')]

def find_start(maze):
    for i in range(0, len(maze[0])):
        if maze[0][i] == '.':
            return i, 0
    return -1, -1

def find_exit(maze):
    for i in range(0, len(maze[0])):
        if maze[len(maze)-1][i] == '.':
            return i, len(maze)-1
    return -1,-1

def longest_path(maze):
    # This sounds like A* but with longest path length. 
    # Could also find all possible paths and maximize distance (?)
    # More on A*: https://www.geeksforgeeks.org/a-search-algorithm/
    start_x, start_y = find_start(maze)
    end_x, end_y = find_exit(maze)

    print(start_x, start_y)
    print(end_x, end_y)
    return 0

def solve_part_one(filename):
    return longest_path(parse_input(filename))

solve_part_one("day23_test.txt")
solve_part_one("day23.txt")
