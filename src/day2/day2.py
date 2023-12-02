# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. 
# What is the sum of the IDs of those games?
 
def parse_game(line):
    game_id = line[0]
    line = line[1:]
    
    blue_terms = 0
    red_terms = 0
    green_terms = 0

    for term in range(0, len(line)-1):
        if line[term + 1] == "blue":
            if int(line[term]) > 14:
                return (game_id, False)
        if line[term + 1] == "red":
            if int(line[term]) > 12:
                return (game_id, False)
        if line[term + 1] == "green":
            if int(line[term]) > 13:
                return (game_id, False)
    return (game_id, True)

def solve_part_one(filename):
    return sum(list(map(lambda game: int(game[0]) if game[1] else 0, list(map(lambda x: parse_game(x), [line.strip("\r\n").replace(":","").replace(",", "").replace(";", "").split(" ")[1:] for line in open(filename, "r")])))))
    
    
print(solve_part_one("day2.txt"))