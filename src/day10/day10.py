
up = (-1,0)
down = (1,0)
left = (0,-1)
right = (0,1)

# Mapping of tile to possible moves 
tiles = {
    '.': [],
    '|': [up, down],
    '-': [left, right],
    'L': [up, right],
    'J': [up, left],
    '7': [down, left],
    'F': [down, right],
    'S': [up, down, left, right]
}

def print_maze(maze):
    for i in range(len(maze)):
        print(''.join(maze[i]))

def find_start(maze):
    """
    Find starting position of animal in the pipe maze.

    Args:
        maze (list): 2D matrix containing pipe locations as characters

    Returns:
        (tuple): (row position of start, column position of start):
    """
    for x in range(0, len(maze)):
        for y in range(0, len(maze[0])):
            if(maze[x][y] == 'S'):
                return x, y
    return -1, -1


def traverse_maze(data, start, direction):
    """
    Traverse pipe map, tracking distance from the initial start position

    Args:
        data (list): Pipe map data (2D character array)
        start (tuple): Starting coordinates for traversal (x, y)
        direction (tuple): Direction vector with which the starting 
                            position should be modified
    
    Returns:
        (tuple): (Distance from starting position, All nodes visited)
    """
    distance = 0
    (x,y) = start

    # Set of visited nodes
    visited = set() 
    
    while distance == 0 or (x,y) != start:
        visited.add((x,y))
        (dx, dy) = direction
        
        # Add position delta to initial coordinates
        x += dx
        y += dy

        # New position is outside of the maze
        if not (0 <= x < len(data) and 0 <= y < len(data[0])):
            return None
        
        dx *= -1
        dy *= -1
        tile_direction = tiles[data[x][y]]
        
        if (dx,dy) not in tile_direction:
            return None
        
        for next_direction in tile_direction:
            if next_direction != (dx,dy):
                direction = next_direction
        distance += 1
    return (distance, visited)

def shoelace_formula(visited):
    area = 0
    for index in range(len(visited)):
        area += (visited[index][0] * visited[(index + 1) % len(visited)][1]) - (visited[index][1] * visited[(index + 1) % len(visited)][0])
    return abs(area) / 2

def picks_theorem(points, area):
    return area - (points / 2) + 1

def solve_part_one(filename):
    # *Heavily* based on a post by 'RedTwinkleToes' on the solution page for Day 10.
    # https://www.reddit.com/r/adventofcode/comments/18evyu9/2023_day_10_solutions/
    maze = [line for line in open(filename, 'r')]
    S = []

    for (dx,dy) in [up, down, left, right]:
        result = traverse_maze(maze, find_start(maze), (dx,dy))
        if result is not None:
            S.append((dx, dy))
            break
    tiles["S"] = S
    return result[0] // 2

def solve_part_two(filename):
    maze = [line for line in open(filename, 'r')]

    for (dx,dy) in [up, down, left, right]:
        result = traverse_maze(maze, find_start(maze), (dx,dy))
        if result is not None:
            break

    pts, visited = result
    visited = list(visited)
    return picks_theorem(pts // 2, shoelace_formula(visited))
    
print(solve_part_two("day10_test.txt"))