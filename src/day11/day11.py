def solve(filename, factor):
    image = [[char for char in line.strip('\n')] for line in open(filename, 'r')]
    
    empty_rows = set()
    # Find empty rows (no '#')
    for i in range(0, len(image)):
        if '#' not in image[i]:
            empty_rows.add(i)
    print(empty_rows)

    # Find empty columns (no '#')
    empty_cols = set()
    for i in range(0, len(image[0])):
        col = [image[j][i] for j in range(len(image))]
        if '#' not in col:
            empty_cols.add(i)
    print(empty_cols)

    galaxies = set()
    # Find galaxies
    for row in range(0, len(image)):
        for column in range(0, len(image[0])):
            if image[row][column] == '#':
                galaxies.add((row,column))
    distances = []

    for galaxy in galaxies:
        for other_galaxy in galaxies - set([galaxy]):
            distance = abs(galaxy[0] - other_galaxy[0]) + abs(galaxy[1] - other_galaxy[1])
            for row in empty_rows:
                if galaxy[0] < row < other_galaxy[0] or other_galaxy[0] < row < galaxy[0]:
                    distance += (factor - 1)
            for col in empty_cols:
                if galaxy[1] < col < other_galaxy[1] or other_galaxy[1] < col < galaxy[1]:
                    distance += (factor - 1)
            distances.append(distance)
    return sum(distances) // 2


def solve_part_one(filename):
    return solve(filename, 2)

def solve_part_two(filename):
    return solve(filename, 1000000)

print(solve_part_one("day11.txt"))
print(solve_part_two("day11.txt"))