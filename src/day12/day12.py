def solve_part_one(filename):
    # Retrieve lines from the file
    lines = [line.strip("\n") for line in open(filename, 'r')]
    
    # Filter lines without a '?' character
    lines = list(filter(lambda x: "?" in x, lines))
    print(lines)

solve_part_one("day12_test.txt")