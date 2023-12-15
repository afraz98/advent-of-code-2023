def find_permutations(line):
    characters, counts = line.split(" ")
    return 0

def solve_part_one(filename):
    # Retrieve lines from the file
    lines = [line.strip("\n") for line in open(filename, 'r')]
    
    # Filter lines without a '?' character
    lines = list(filter(lambda x: "?" in x[0], lines))
    
    return sum([find_permutations(line) for line in lines])

print(solve_part_one("day12_test.txt"))