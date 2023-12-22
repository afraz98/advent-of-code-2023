def parse_input(filename):
    return [[c for c in line] for line in open(filename, 'r').read().splitlines()]

def print_map(map):
    for row in range(len(map)):
        print(''.join(map[row]))
    pass

def traverse_map(map):
    # TODO: For some reason this loops infinitely...
    visited = set()
    photons = [(0,0,1,0)]

    while photons != []:
        x, y, dx, dy = photons.pop(0)
        # print(y, x, dx, dy)

        if x < 0 or x >= len(map[0]):
            continue
        
        if y < 0 or y >= len(map):
            continue

        visited.add((x,y)) 

        if map[y][x] == ".":
            photons.append((x + dx, y + dy, dx, dy))

        if map[y][x] == "-":
            if dy != 0: # Approaching from top/bottom
                photons.append((x+1, y, 1, 0))
                photons.append((x-1, y, -1, 0))
            else:       # Continue as normal
                photons.append((x + dx, y+dy, dx, dy))
        
        if map[y][x] == "|":
            if dx != 0: # Approaching from either side
                photons.append((x, y+1, 0, 1))
                photons.append((x, y-1, 0, -1))
            else:       # Continue as normal                
                photons.append((x, y + dy, 0, dy))
        
        if map[y][x] == "\\":
            if dx > 0:
                photons.append((x, y + 1, 0, 1))
            if dx < 0:
                photons.append((x, y - 1, 0, -1))
            if dy > 0:
                photons.append((x + 1, y, 1, 0))
            if dy < 0:
                photons.append((x - 1, y, -1, 0))
            
        if map[y][x] == "/":
            if dx > 0:
                photons.append((x, y - 1, 0, -1))
            if dx < 0:
                photons.append((x, y + 1, 0, 1))
            if dy > 0:
                photons.append((x - 1, y, -1, 0))
            if dy < 0:
                photons.append((x + 1, y, 1, 0))
        print(len(visited))
    return len(visited)

def solve_part_one(filename):
    map = parse_input(filename)
    print_map(map)
    return traverse_map(map)

print(solve_part_one("day16.txt"))
