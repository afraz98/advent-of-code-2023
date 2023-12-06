def tally_points(games):
    sum = 0
    for game in games:
        points = 0
        
        game = list(filter(lambda x: x != '', game))[2:]
        winning_numbers, actual_numbers = ":".join(game).split("|")

        winning_numbers = list(filter(lambda x: x != '', winning_numbers.split(":")))
        actual_numbers = list(filter(lambda x: x != '', actual_numbers.split(":")))

        for number in actual_numbers:
            if number in winning_numbers:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        sum += points
    return sum

def tally_cards(games):
    number_of_cards = 0
    active_games = [game for game in games]

    while active_games != []:
        points = 0
        index = 0

        active_game = list(filter(lambda x: x != '', active_games[0]))
        winning_numbers, actual_numbers = ":".join(active_game[2:]).split("|")

        winning_numbers = list(filter(lambda x: x != '', winning_numbers.split(":")))
        actual_numbers = list(filter(lambda x: x != '', actual_numbers.split(":")))

        for number in actual_numbers:
            if number in winning_numbers:
                points += 1

        print(active_game[0], active_game[1], winning_numbers, actual_numbers, points)

        # Find original card that is the (index + i) index after the active game's id
        for game in games:
            if game[1] == active_game[1]: # Same game IDs
                index = games.index(game)

        for i in range(1, points + 1):
            active_games.append(games[index + i])

        active_games.pop(0)
        number_of_cards += 1

    return number_of_cards

def solve_part_one(filename):
    return tally_points([line.strip("\r\n").replace(":", "").split(" ") for line in open(filename, 'r')])

def solve_part_two(filename):
    return tally_cards([line.strip("\r\n").replace(":", "").split(" ") for line in open(filename, 'r')])


print(solve_part_one("day4.txt"))
print(solve_part_two("day4.txt"))