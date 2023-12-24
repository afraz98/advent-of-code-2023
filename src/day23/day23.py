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

def depth_first_search(x, y, end_x, end_y, visited, maze):
    visited.add((x,y))
    pass

def traverse_maze(maze, x, y, end_x, end_y):
    visited = set()
    depth_first_search(x, y, end_x, end_y, visited, maze)
    return 0

def longest_path(maze):
    start_x, start_y = find_start(maze)
    end_x, end_y = find_exit(maze)
    return traverse_maze(maze, start_x, start_y, end_x, end_y)

def solve_part_one(filename):
    return longest_path(parse_input(filename))

solve_part_one("day23_test.txt")
solve_part_one("day23.txt")
