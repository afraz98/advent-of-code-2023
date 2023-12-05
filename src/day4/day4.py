def solve_part_one(filename):
    input = [line.strip("\r\n").replace(":", "").split(" ")[1:] for line in open(filename, 'r')]
    
    for game in input:
        game_id = game[0]
        
print(solve_part_one("day4.txt"))