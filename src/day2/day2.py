# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. 
# What is the sum of the IDs of those games?
 
def solve_part_one(filename):
    red_cubes = 12
    green_cubes = 13
    blue_cubes = 14
    lines = [line.strip("\r\n").split(" ") for line in open(filename, "r")]
    print(lines)
    
print(solve_part_one("day2.txt"))