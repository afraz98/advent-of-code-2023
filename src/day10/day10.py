
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

def is_valid(maze, number_rows, number_columns, x, y, previous_color, new_color):
    if x < 0 or x >= number_rows-1 or y < 0 or y >= number_columns-1: 
        return False
    if maze[x][y]!= previous_color or maze[x][y]== new_color:
        return False
    return True

# Flood Fill algorithm adapted from here: https://www.geeksforgeeks.org/flood-fill-algorithm/
def flood_fill_maze(map, number_rows, number_columns, x, y, previous_color, new_color):
    queue = []
     
    # Append the position of starting pixel of the component
    queue.append([x, y])
 
    # Color the pixel with the new color
    map[x][y] = new_color
 
    # While the queue is not empty, i.e. the whole component has the 'previous' color
    while queue != []:
         
        # Dequeue the front node
        currPixel = queue.pop()
         
        posX = currPixel[0]
        posY = currPixel[1]
         
        # Check if the adjacent pixels are valid
        if is_valid(map, number_rows, number_columns, posX + 1, posY, previous_color, new_color):
             
            # Color with new_color if valid and enqueue
            map[posX + 1][posY] = new_color
            queue.append([posX + 1, posY])
         
        if is_valid(map, number_rows, number_columns, posX-1, posY, previous_color, new_color):
            map[posX-1][posY]= new_color
            queue.append([posX-1, posY])
         
        if is_valid(map, number_rows, number_columns, posX, posY + 1, previous_color, new_color):
            map[posX][posY + 1]= new_color
            queue.append([posX, posY + 1])
         
        if is_valid(map, number_rows, number_columns, posX, posY-1, previous_color, new_color):
            map[posX][posY-1]= new_color
            queue.append([posX, posY-1])
    pass

def solve_part_one(filename):
    # *Heavily* based on a post by 'RedTwinkleToes' on the solution page for Day 10.
    # https://www.reddit.com/r/adventofcode/comments/18evyu9/2023_day_10_solutions/
    maze = [line for line in open(filename, 'r')]
    
    for (dx,dy) in [up, down, left, right]:
        result = traverse_maze(maze, find_start(maze), (dx,dy))
        if result is not None:
            break

    return result[0] // 2

def find_interior_points(points, area):
    return area - (len(points) // 2) + 1

def area(points):
    # Calculate area via Shoelace formula: https://en.wikipedia.org/wiki/Shoelace_formula
    area = 0
    for i in range(len(points)):
        area += (points[i % len(points)][0]*points[(i+1) % len(points)][0]) - (points[i % len(points)][1] * points[(i+1) % len(points)][1])
    return area // 2

def solve_part_two(filename):
    maze = [line for line in open(filename, 'r')]
    highlighted_maze = [[character for character in line.strip('\n')] for line in open(filename, 'r')]

    for (dx,dy) in [up, down, left, right]:
        result = traverse_maze(maze, find_start(maze), (dx,dy))
        if result is not None:
            break

    _, visited = result
    visited = list(visited)

    for coordinate in visited:
        highlighted_maze[coordinate[0]][coordinate[1]] = 'X'
    
    for i in range(0, len(highlighted_maze)):
        print(''.join(highlighted_maze[i]))

    _area = area(sorted(visited))

    for i in range(0, len(highlighted_maze)):
        print(''.join(highlighted_maze[i]))
    
    return find_interior_points(visited, _area)
    
print(solve_part_one("day10.txt"))
print(solve_part_two("day10_test_2.txt"))