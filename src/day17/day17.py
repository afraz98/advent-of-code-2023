import sys

class Graph():
    def __init__(self):
        self.nodes = []

    def add_node(self, x, y, distance):
        self.nodes.append(Node(x, y, distance))
        pass

class Node():
    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.distance = distance

def parse_input(filename):
    return [[character for character in line.strip('\n')] for line in open(filename, 'r')]

def print_maze(maze):
    for i in range(len(maze)):
        print(''.join(maze[i]))

# This will probably need to be a variant of A* (see here: https://www.geeksforgeeks.org/a-search-algorithm/)
def find_minimum_heat_loss(maze, x, y, moves_in_direction, total_heat_loss):
    if moves_in_direction > 3:
        return 999

    if x > len(maze):
        return 999

    if y > len(maze[0]):
        return 999

    return 10
def solve_part_one(filename):
    maze = parse_input(filename)
    return find_minimum_heat_loss(maze, 0, 0, 0, 0)


print(solve_part_one("day17_test.txt"))