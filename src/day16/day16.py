def parse_input(filename):
    return [[c for c in line] for line in open(filename, 'r').read().splitlines()]

def print_map(map):
    for row in range(len(map)):
        print(''.join(map[row]))
    pass

def traverse_map(sx, sy, sdx, sdy, matrix):
    visited = set()
    photons = [(sx, sy, sdx, sdy)]

    while photons != []:
        x, y, dx, dy = photons.pop()
        
        if x < 0 or x >= len(matrix[0]):
            continue
        
        if y < 0 or y >= len(matrix):
            continue

        visited.add((x, y, dx, dy)) 

        if matrix[y][x] == ".":
            if (x + dx, y + dy, dx, dy) not in visited:
                photons.append((x + dx, y + dy, dx, dy))

        if matrix[y][x] == "-":
            if dy != 0:
                if (x+1, y, 1, 0) not in visited:
                    photons.append((x+1, y, 1, 0))
                if (x-1, y, -1, 0) not in visited:
                    photons.append((x-1, y, -1, 0))
            else:
                if (x + dx, y+dy, dx, dy) not in visited:
                    photons.append((x + dx, y+dy, dx, dy))
        
        if matrix[y][x] == "|":
            if dx != 0:
                if (x, y+1, 0, 1) not in visited:
                    photons.append((x, y+1, 0, 1))
                
                if (x, y-1, 0, -1) not in visited:
                    photons.append((x, y-1, 0, -1))
            else:
                if (x, y + dy, 0, dy) not in visited:          
                    photons.append((x, y + dy, 0, dy))

        if matrix[y][x] == "\\":
            if dx > 0:
                if (x, y + 1, 0, 1) not in visited:
                    photons.append((x, y + 1, 0, 1))
            if dx < 0:
                if (x, y - 1, 0, -1) not in visited:
                    photons.append((x, y - 1, 0, -1))
            if dy > 0:
                if (x + 1, y, 1, 0) not in visited:
                    photons.append((x + 1, y, 1, 0))
            if dy < 0:
                if (x - 1, y, -1, 0) not in visited:
                    photons.append((x - 1, y, -1, 0))
            
        if matrix[y][x] == "/":
            if dx > 0:
                if (x, y - 1, 0, -1) not in visited:
                    photons.append((x, y - 1, 0, -1))
            if dx < 0:
                if (x, y + 1, 0, 1) not in visited:
                    photons.append((x, y + 1, 0, 1))
            if dy > 0:
                if (x - 1, y, -1, 0) not in visited:
                    photons.append((x - 1, y, -1, 0))
            if dy < 0:
                if (x + 1, y, 1, 0) not in visited:
                    photons.append((x + 1, y, 1, 0))
    return len(set(map(lambda x: (x[0], x[1]), visited)))

def solve_part_one(filename):
    return traverse_map(0, 0, 1, 0, parse_input(filename))

def solve_part_two(filename):
    map = parse_input(filename)
    return max([traverse_map(x, y, dx, dy, map) for (x,y,dx,dy) in [(x, 0, 0, 1) for x in range(0, len(map[0]))] + [(x, len(map), 0, -1) for x in range (0, len(map[0]))] + [(0, y, 1, 0) for y in range(0, len(map))] + [(len(map[0])-1, y, -1, 0) for y in range(0, len(map))]])

print(solve_part_one("day16_test.txt"))
print(solve_part_two("day16.txt"))