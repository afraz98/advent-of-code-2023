# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. 
# What is the sum of the IDs of those games?
 
def parse_game(game):
    game_id = game[0]
    game = game[1:]
    
    test_map = dict(zip(['blue', 'red', 'green'], [14, 12, 13]))
    
    for term in range(0, len(game)-1):
        for color in test_map.keys():
            if game[term + 1] == color:
                if int(game[term]) > test_map[color]:
                    return (game_id, False)

    return (game_id, True)

def solve_part_one(filename):
    return sum(list(map(lambda game: int(game[0]) if game[1] else 0, list(map(lambda x: parse_game(x), [line.strip("\r\n").replace(":","").replace(",", "").replace(";", "").split(" ")[1:] for line in open(filename, "r")])))))
    
def parse_game_part_two(game):
    game_id = game[0]
    game = game[1:]

    test_map = dict(zip(['blue', 'red', 'green'], [0, 0, 0]))

    for term in range(0, len(game)-1):
        for color in test_map.keys():
            if game[term + 1] == color:
                test_map[color] = max(test_map[color], int(game[term]))

    return (game_id, test_map['blue'], test_map['green'], test_map['red'])

def solve_part_two(filename):
    return sum(list(map(lambda game: game[1]*game[2]*game[3], list(map(lambda x: parse_game_part_two(x), [line.strip("\r\n").replace(":","").replace(",", "").replace(";", "").split(" ")[1:] for line in open(filename, "r")])))))

print(solve_part_one("day2.txt"))
print(solve_part_two("day2.txt"))