def parse_input(filename):
    return [line.strip('\n') for line in open(filename, 'r')]

def parse_instruction(instruction, current_position, vertices):
    direction, distance, color = instruction.split(" ")
    vertices.append(current_position)
    if direction == 'D':
        for x in range(int(distance)):
            current_position = (current_position[0] + 1, current_position[1])
            vertices.append(current_position)
    
    if direction == 'U':
        for x in range(int(distance)):
            current_position = (current_position[0] - 1, current_position[1])
            vertices.append(current_position)
        
    if direction == 'L':
        for x in range(int(distance)):
            current_position = (current_position[0], current_position[1] - 1)
            vertices.append(current_position)
    
    if direction == 'R':
        for x in range(int(distance)):
            current_position = (current_position[0], current_position[1] + 1)
            vertices.append(current_position)
    return current_position
    
def is_valid(screen, number_rows, number_cols, x, y, previous_color, new_color):
    if x < 0 or x >= number_rows or y < 0 or y >= number_cols or screen[x][y]!= previous_color or screen[x][y]== new_color:
        return False
    return True

# Flood-Fill algorithm adapted from here: https://www.geeksforgeeks.org/flood-fill-algorithm/ 
def flood_fill(area, number_rows, number_cols, x, y, previous_color, new_color):
    queue = []
     
    # Append the position of starting 
    # pixel of the component
    queue.append([x, y])
 
    # Color the pixel with the new color
    area[x][y] = new_color
 
    # While the queue is not empty i.e. the whole component having previous_color is not colored with new_color
    while queue:
         
        # Dequeue the front node
        currPixel = queue.pop()
         
        posX = currPixel[0]
        posY = currPixel[1]
         
        # Check if the adjacent pixels are valid
        if is_valid(area, number_rows, number_cols, posX + 1, posY, previous_color, new_color):
            # Color with new color if valid and enqueue
            area[posX + 1][posY] = new_color
            queue.append([posX + 1, posY])
         
        if is_valid(area, number_rows, number_cols, posX-1, posY, previous_color, new_color):
            area[posX-1][posY] = new_color
            queue.append([posX-1, posY])
         
        if is_valid(area, number_rows, number_cols, posX, posY + 1, previous_color, new_color):
            area[posX][posY + 1] = new_color
            queue.append([posX, posY + 1])
         
        if is_valid(area, number_rows, number_cols, posX, posY-1, previous_color, new_color):
            area[posX][posY-1] = new_color
            queue.append([posX, posY-1])

def solve_part_one(filename):
    instructions = parse_input(filename)
    vertices = []
    corrected_vertices = []
    current_position = (0,0)

    # Find vertices of the dig site
    for instruction in instructions:
        current_position = parse_instruction(instruction, current_position, vertices)

    y_factor = sorted(vertices, key=lambda x: x[1])[0][1]
    x_factor = sorted(vertices, key=lambda x: x[0])[0][0]

    for l in range(len(vertices)):
        corrected_vertices.append((vertices[l][0] + abs(x_factor), vertices[l][1] + abs(y_factor)))

    dig_site = [["." for i in range(500) ] for j in range(500)]
    print(len(dig_site), len(dig_site[0]))
    for position in corrected_vertices:
        print(position[0], position[1])
        dig_site[position[0]][position[1]] = '#'
        
    # Use Flood-Fill algorithm to fill in the center of the dig site
    flood_fill(dig_site, len(dig_site), len(dig_site[0]), corrected_vertices[-1][0], corrected_vertices[-1][1], ".", "#")
    
    for j in range(len(dig_site)):
       print(''.join(dig_site[j]))

    count = 0
    for j in range(len(dig_site)):
        for i in range(len(dig_site[0])):
            if dig_site[j][i] == "#":
                count += 1
    return count

print(solve_part_one("day18.txt"))