
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


def solve_part_one(filename):
    # *Heavily* based on a post by 'RedTwinkleToes' on the solution page for Day 10.
    # https://www.reddit.com/r/adventofcode/comments/18evyu9/2023_day_10_solutions/
    maze = [line for line in open(filename, 'r')]
    
    for (dx,dy) in [up, down, left, right]:
        result = traverse_maze(maze, find_start(maze), (dx,dy))
        if result is not None:
            break

    print(result[0] // 2)

def solve_part_two(filename):
    # TODO: (1) Probably want to implement something similar to what is described here:
    #           https://stackoverflow.com/questions/217578/how-can-i-determine-whether-a-2d-point-is-within-a-polygon
    #       (2) Or a Flood-Fill algorithm? https://www.geeksforgeeks.org/flood-fill-algorithm/
    #       (3) Or Pick's theorem? https://en.wikipedia.org/wiki/Pick's_theorem
    #       (4) Or the Shoelace formula? https://en.wikipedia.org/wiki/Shoelace_formula
    maze = [line for line in open(filename, 'r')]
    highlighted_maze = [[character for character in line] for line in open(filename, 'r')]

    for (dx,dy) in [up, down, left, right]:
        result = traverse_maze(maze, find_start(maze), (dx,dy))
        if result is not None:
            break

    _, visited = result
    print(visited)

    for coordinate in visited:
        highlighted_maze[coordinate[0]][coordinate[1]] = 'X'
    
    for i in range(0, len(highlighted_maze)):
        for j in range(0, len(highlighted_maze[0])):
            print(highlighted_maze[i][j], end='')
    pass
    
solve_part_one("day10.txt")
solve_part_two("day10_test_2.txt")