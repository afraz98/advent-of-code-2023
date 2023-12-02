# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. 
# What is the sum of the IDs of those games?
 
def parse_game(game):
    game_id = game[0]
    game = game[1:]
    
    test_map = dict(zip(['blue', 'red', 'green'], [14, 13, 12]))

    for term in range(0, len(game)-1):
        if game[term + 1] == "blue":
            if int(game[term]) > 14:
                return (game_id, False)
        if game[term + 1] == "red":
            if int(game[term]) > 12:
                return (game_id, False)
        if game[term + 1] == "green":
            if int(game[term]) > 13:
                return (game_id, False)
    return (game_id, True)

def solve_part_one(filename):
    return sum(list(map(lambda game: int(game[0]) if game[1] else 0, list(map(lambda x: parse_game(x), [line.strip("\r\n").replace(":","").replace(",", "").replace(";", "").split(" ")[1:] for line in open(filename, "r")])))))
    
def parse_game_part_two(game):
    game_id = game[0]
    game = game[1:]
    
    max_blue = 0
    max_red = 0
    max_green = 0

    for term in range(0, len(game)-1):
        if game[term + 1] == "blue":
            max_blue = max(max_blue, int(game[term]))
        if game[term + 1] == "red":
            max_red = max(max_red, int(game[term]))
        if game[term + 1] == "green":
            max_green = max(max_green, int(game[term]))
    return (game_id, max_blue, max_green, max_red)

def solve_part_two(filename):
    return sum(list(map(lambda game: game[1]*game[2]*game[3], list(map(lambda x: parse_game_part_two(x), [line.strip("\r\n").replace(":","").replace(",", "").replace(";", "").split(" ")[1:] for line in open(filename, "r")])))))

print(solve_part_one("day2.txt"))
print(solve_part_two("day2.txt"))